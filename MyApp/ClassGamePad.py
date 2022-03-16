import pygame
from ClassAbstractHardware import ClassAbstractHardware


class ClassGamePad(ClassAbstractHardware):

    def __init__(self):
        super().__init__()
        self.axis0 = None
        self.axis1 = None

    def _connect(self, device):
        pygame.init()
        pygame.joystick.init()  # Initialize the joysticks.

        # Get count of joysticks.
        joystick_count = pygame.joystick.get_count()
        print('Found ' + str(joystick_count) + ' joysticks.')
        if joystick_count < 1:
            print('No joysticks found. Cannot connect!')
            return False

        # init joystick
        self.joystick = pygame.joystick.Joystick(device)
        self.joystick.init()

        # Get the name from the OS for the controller/joystick.
        joystick_name = self.joystick.get_name()
        print('Connected to ' + joystick_name)

        number_axes = self.joystick.get_numaxes()
        return True

    def _disconnect(self):
        pygame.quit()
        return True

    def _getData(self):
        self.axis0 = self.joystick.get_axis(0)
        self.axis1 = self.joystick.get_axis(1)
        pygame.event.pump()
        return True

    def _setData(self):
        print('Cannot write anything to camera!')
        return False
