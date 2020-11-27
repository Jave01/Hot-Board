# ******************************************
# file: vcp_handler.py
# project: Hot-Board
# author: Nils Jäggi
# description: communication with the Hardware itself
# ******************************************
import serial  # python -m pip install pyserial
from serial.tools import list_ports



class VirtualComPort():
    def __init__(self, switch_Identifier: str, number_of_digits: int):
        # protocol constants
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
        self.is_connected = False

    def start_hot_board(self, com: str = '', baud: int = 115200) -> bool:
        """ searches for a connected board and tries to connect.
            COM port and baudrate can be changed manually if needed

            :returns:
                flag if it worked or not
        """

        possible_ports = self.search_board()
        if com != '':
            self.ser.port = com
            self.ser.baudrate = baud

        if len(possible_ports) > 0:
            for p in possible_ports:
                self.ser.port = p
                try:
                    self.ser.open()
                    print(p)
                except serial.SerialException:
                    continue

        if self.ser.isOpen():
            print('connection established')
            return True
        else:
            return False


    def search_board(self) -> list:
        """Returns a list with all COM ports connected to a STM controller"""
        ports = list_ports.comports()
        possible_ports = []
        for p in ports:
            name = p.description
            # searches for the STM Controller
            if name.startswith('STM') or name.startswith('Seriell') or name.startswith('serial'):
                possible_ports.append(p.device)

        return possible_ports


    def check_switch_state(self) -> str:
        """Reads the serial buffer and searches for a string which matches the key format"""
        try:
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
        except serial.SerialException:
            print('Board plugged out')
            if self.ser.isOpen():
                self.ser.close()


    def get_buffer_value(self) -> str:
        """Returns serial buffer converted to Ascii"""
        serData = self.ser.read(256).decode('ascii')
        return serData
