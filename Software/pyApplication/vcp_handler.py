# ******************************************
# file: vcp_handler.py
# project: Hot-Board
# author: Nils Jäggi
# description: communication with the Hardware itself
# ******************************************
import glob
import sys
import serial  # python -m pip install pyserial
from serial.tools import list_ports
import glob


class VirtualComPort():
    def __init__(self, switch_Identifier: str, number_of_digits: int):
        # protocoll constants
        self.numberOfDigits = number_of_digits
        self.switchIdentifier = switch_Identifier

        # Initialize the serial object
        self.ser = serial.Serial(
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=0,
            xonxoff=False,
            rtscts=False,
            dsrdtr=False,
            writeTimeout=2
        )

    def start_hot_board(self, com: str = '', baud: int = 115200) -> bool:
        """ searches for a connected board and tries to connect.
            COM Port and baudrate can be changed manually if needed

            :returns:
                flag if it worked or not
        """
        if com == '':
            ports = list_ports.comports()
            for p in ports:
                name = p.description
                # searches for the STM Controller, it is named different on different OS
                # And it depends on the OS language
                if name.startswith('STM') or name.startswith('Seriell') or name.startswith('serial'):
                    self.ser.port = p.device
                    self.ser.baudrate = baud
                    break
        else:
            self.ser.port = com
            self.ser.baudrate = baud

        try:
            self.ser.open()
            print('connection established')
            return True
        except serial.SerialException:
            return False

    def check_switch_state(self) -> str:
        """Reads the serial buffer and searches for a string which matches the
        key format (for example s1) """
        serData = self.ser.read(len(self.switchIdentifier) + self.numberOfDigits).decode('ascii')
        # if data is valid
        if self.switchIdentifier in serData:
            # get the switch number. can be 1 or more digits
            retVal = 0
            for i in range(self.numberOfDigits):
                retVal += int(serData[(i + 1) * (-1)]) * pow(10, i)
            return 's' + str(retVal)
        else:
            return ''

    def get_serial_ports(self) -> bool:
        """ Returns a list of serial devices"""
        return list_ports.comports()

    def get_buffer_value(self) -> str:
        """Returns serial buffer converted to Ascii"""
        serData = self.ser.read(256).decode('ascii')
        return serData
