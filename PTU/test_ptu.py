#!/usr/bin/env python3
import time

import serial

# -----------------------------------------
# Initialization
# -----------------------------------------

# Configure serial port
ser = serial.Serial()  # open serial port
ser.port = '/dev/ttyUSB0'
ser.baudrate = 9600
ser.parity = serial.PARITY_NONE
ser.bytesize = 8
ser.stopbits = 1

ser.open() # open port

# -----------------------------------------
# Execution (in cycle)
# -----------------------------------------

def sendToPTU(msg_to_send):
    msg_to_send += '\n'
    ser.write(msg_to_send.encode())
    print('Sent: ' + msg_to_send)
    time.sleep(0.02)
    msg_received = ser.read_until().decode()
    print('Received: ' + msg_received)
    return msg_received

while True:

    sendToPTU('PS6000')
    sendToPTU('TS6000')
    sendToPTU('PP5000')
    sendToPTU('TP2500')
    time.sleep(5)

    sendToPTU('PS1000')
    sendToPTU('TS1000')
    sendToPTU('PP-5000')
    sendToPTU('TP-1500')
    time.sleep(10)

# -----------------------------------------
# Termination
# -----------------------------------------
ser.close()
