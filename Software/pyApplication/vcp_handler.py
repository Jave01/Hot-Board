# ******************************************
# file: vcp_handler.py
# project: Hot-Board
# author: Nils Jäggi
# description: communication with the Hardware itself
# ******************************************
import glob
import sys
import serial   # python -m pip install pyserial

class VirtualComPort():
    def __init__(self,switch_Identifier: str ,number_of_digits: int):
        # protocoll constants
        self.numberOfDigits = number_of_digits
        self.switchIdentifier = switch_Identifier
        # create vcp object
        self.ser = serial.Serial()
        
    def start_hot_board(self, com: str, baud: int = 115200) -> bool:
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

    def check_switch_state(self) -> int:
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

    def get_buffer_value(self):
        """Returns serial buffer convertet to Ascii"""
        serData = self.ser.read(256).decode('ascii')
        return serData

    def get_available_serial_ports(self) -> list:
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

