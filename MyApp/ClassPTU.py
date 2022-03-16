import serial

from ClassAbstractHardware import ClassAbstractHardware

class PanTilt():
    def __init__(self):
        self.pan = None
        self.tilt = None

class PositionSpeed():
    def __init__(self):
        self.position = PanTilt()
        self.speed = PanTilt()

class ClassPTU(ClassAbstractHardware):

    def __init__(self):
        super().__init__()
        self.goal = PositionSpeed()

    def _connect(self, device):

        # Configure serial port
        self.serial = serial.Serial()  # open serial port
        self.serial.port = device
        self.serial.baudrate = 38400
        self.serial.parity = serial.PARITY_NONE
        self.serial.bytesize = 8
        self.serial.stopbits = 1

        self.serial.open()  # open port
        return True

    def _disconnect(self):
        self.serial.close()
        return True

    def _getData(self):
        return True

    def _setData(self):
        msg_to_send = 'PP' + str(self.goal.position.pan) + '\n'
        self.serial.write(msg_to_send.encode())
        msg_to_send = 'TP' + str(self.goal.position.tilt) + '\n'
        self.serial.write(msg_to_send.encode())
        return False
