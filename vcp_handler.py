# ******************************************
# file: vcp_handler.py
# project: Hot-Board
# description: communication with the Hardware itself
# ******************************************
import serial   # python -m pip install pyserial

class vcp_reader():
    vcp_baudrate = 9600     # standard baud

    def __init__(self):
        serp = serial.Serial()
        serp.baud = 9600
        #serp.com = port_name
        serp.open()
        print(serp.name)

    def print_info(self):
        print(serp.name)
