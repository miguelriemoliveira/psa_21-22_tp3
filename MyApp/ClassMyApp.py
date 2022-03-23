import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

from ClassGamePad import ClassGamePad
from ClassPTU import ClassPTU

PROJECT_PATH = './'
PROJECT_UI = './MyApp.ui'


class ClassMyApp:

    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)

        # create main window
        self.main_window = builder.get_object('toplevelMain', master)
        self.main_window.resizable(width=False, height=False)
        self.main_window.bind('q', self.callbackCommandExit)
        self.main_window.bind('g', self.callbackGamePadConnect)
        self.main_window.bind('p', self.callbackPTUConnect)

        # Create game pad window
        self.game_pad_window = builder.get_object('toplevelGamePad')
        self.game_pad_window.resizable(width=False, height=False)
        self.game_pad_window.bind('q', self.callbackCommandExit)
        self.game_pad_window.withdraw()

        # Create ptu window
        self.ptu_window = builder.get_object('toplevelPTU')
        self.ptu_window.resizable(width=False, height=False)
        self.ptu_window.bind('q', self.callbackCommandExit)
        self.ptu_window.withdraw()

        builder.connect_callbacks(self)

        # Instantiate hardware communication classes
        self.game_pad = ClassGamePad()
        self.ptu = ClassPTU()
        self.ptu.goal.position.pan = 0
        self.ptu.goal.position.tilt = 0

    # PTU callbacks
    def callbackPTUConnect(self, key=None):
        self.ptu_window.deiconify()
        self.ptu.connect('/dev/ttyUSB0')
        self.callbackPTUTimer()

    def callbackPTUDisconnect(self):
        self.ptu_window.withdraw()
        self.ptu.disconnect()

    def callbackPTUTimer(self):

        self.ptu.setData()
        self.ptu.getData()

        self.builder.get_variable('entryPTUPanMonitorText').set(str(self.ptu.current.position.pan))
        self.builder.get_variable('entryPTUTiltMonitorText').set(str(self.ptu.current.position.tilt))

        self.builder.get_variable('entryPTUPanGoalMonitorText').set(str(self.ptu.goal.position.pan))
        self.builder.get_variable('entryPTUTiltGoalMonitorText').set(str(self.ptu.goal.position.tilt))

        # ask the window to call the same functiona again after x milisecs
        self.ptu_window.after(200, self.callbackPTUTimer)

    def callbackScalePTUPanManualControl(self, value):
        value = int(float(value))
        self.ptu.goal.position.pan = value

    def callbackScalePTUTiltManualControl(self, value):
        value = int(float(value))
        self.ptu.goal.position.tilt = value

    # Game Pad callbacks
    def callbackGamePadConnect(self, key=None):
        self.game_pad_window.deiconify()
        self.game_pad.connect(0)
        self.callbackGamePadTimer()

    def callbackGamePadDisconnect(self):
        self.game_pad_window.withdraw()
        self.game_pad.disconnect()

    def callbackGamePadTimer(self):
        self.game_pad.getData()
        # print('Axis0=' + str(self.game_pad.axis0) + '   Axis1=' + str(self.game_pad.axis1))
        formatted_axis0 = round(self.game_pad.axis0 * 100)/100
        formatted_axis1 = round(self.game_pad.axis1 * 100)/100

        self.builder.get_variable('entryAxis0TextVariable').set(str(formatted_axis0))
        self.builder.get_variable('entryAxis1TextVariable').set(str(formatted_axis1))

        # ask the window to call the same functiona again after x milisecs
        self.game_pad_window.after(100, self.callbackGamePadTimer)


    # Main window callbacks
    def callbackCommandExit(self, key=None):
        print('Bye bye!')
        exit(0)

    def run(self):
        self.main_window.mainloop()




