# ******************************************
# file: vcp_handler.py
# project: Hot-Board
# author: Nils Jäggi
# description: communication with the Hardware itself
# ******************************************
import sys
import glob
import serial   # python -m pip install pyserial

import sys
import time
import serial

class VirtualComPort():
    def __init__(self,switch_Identifier,number_of_digits):
        # protocoll constants
        self.numberOfDigits = number_of_digits
        self.switchIdentifier = switch_Identifier
        # create vcp object
        self.ser = serial.Serial()
        
    def start_hot_board(self,com,baud):
        """ opens the comport

            :returns:
                flag if it worked or not
        """
        self.ser.port = com
        self.ser.baudrate = baud
        self.ser.timeout = 0
        # try opening vcp
        try:
            self.ser.open()
            return True
        except serial.SerialException:
            return False

    def check_switch_state(self):
        # read serial port buffer
        serData = self.ser.read( len(self.switchIdentifier)+self.numberOfDigits ).decode('ascii')
        # if data is valid
        if self.switchIdentifier in serData:
            # get the switch number. can be 1 or more digits
            retVal = 0
            for i in range(self.numberOfDigits):
                retVal += int( serData[(i+1)*(-1)] ) * pow(10,i)
            return retVal
        else:
            return -1

    def get_available_serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result

"""boi = vcpboi('switch',1)
print(boi.get_available_serial_ports())
print(boi.start_hot_board('COM3',115200))

while True:
    state = boi.check_switch_state()
    if state != -1:
        print(state)
    time.sleep(0.5)"""
        