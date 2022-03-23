import time

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
        self.current = PositionSpeed()
        self.previous_msg = ''

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

        msg_to_send = 'PP\n'
        self.serial.write(msg_to_send.encode())
        msg_to_send = 'TP\n'
        self.serial.write(msg_to_send.encode())
        msg_to_send = 'PS\n'
        self.serial.write(msg_to_send.encode())
        msg_to_send = 'TS\n'
        self.serial.write(msg_to_send.encode())
        time.sleep(0.1)

        data_received = self.serial.read_all()

        try:
            data_received = data_received.decode()
        except:
            print('Could not decode msg received.')
            return

        # print('data_received=\n' + str(data_received) + '\n\n')

        data_received = self.previous_msg + data_received

        msgs = data_received.split('\n')
        # print('msgs=\n' + str(msgs) + '\n\n')

        self.previous_msg = msgs[-1]

        for msg in msgs:
            msg = msg.strip('\r')
            # print('Analysing msg=\n' + str(msg))

            if 'Current Pan position is' in msg:
                # print('This msg is about position pan')
                self.current.position.pan = self.findNumber(msg)
            elif 'Current Tilt position is' in msg:
                # print('This msg is about position tilt')
                self.current.position.tilt = self.findNumber(msg)
            elif 'Target Pan speed is' in msg:
                # print('This msg is about speed pan')
                self.current.speed.pan = self.findNumber(msg)
            elif 'Target Tilt speed is' in msg:
                # print('This msg is about speed tilt')
                self.current.speed.tilt = self.findNumber(msg)

        print('current ptu state:')
        print('current.position.pan=' + str(self.current.position.pan))
        print('current.position.tilt=' + str(self.current.position.tilt))
        print('current.speed.pan=' + str(self.current.speed.pan))
        print('current.speed.tilt=' + str(self.current.speed.tilt))

        return True

    def findNumber(self, text):
        words = text.split(' ')
        # print('words: ' + str(words))
        for word in words:
            try:
                number = int(word)
                # print(word + ' IS A NUMBER!')
                return number
            except:
                # print(word + ' is not a number!')
                pass

        return None

    def _setData(self):
        msg_to_send = 'PP' + str(self.goal.position.pan) + '\n'
        self.serial.write(msg_to_send.encode())
        msg_to_send = 'TP' + str(self.goal.position.tilt) + '\n'
        self.serial.write(msg_to_send.encode())
        return True
