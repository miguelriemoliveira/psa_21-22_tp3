#!/usr/bin/env python3
import time
from ClassPTU import ClassPTU
# -----------------------------------------
# Initialization
# -----------------------------------------

ptu = ClassPTU()
ptu.connect('/dev/ttyUSB0')

# -----------------------------------------
# Execution (in cycle)
# -----------------------------------------

# def sendToPTU(msg_to_send):
#     msg_to_send += '\n'
#     ser.write(msg_to_send.encode())
#     print('Sent: ' + msg_to_send)
#     time.sleep(0.02)
#     msg_received = ser.read_until().decode()
#     print('Received: ' + msg_received)
#     return msg_received

while True:

    ptu.goal.position.pan = 5000
    ptu.goal.position.tilt = -1500
    ptu.setData()
    time.sleep(5)

    ptu.goal.position.pan = -5000
    ptu.goal.position.tilt = 1500
    ptu.setData()
    time.sleep(5)

# -----------------------------------------
# Termination
# -----------------------------------------
