# ******************************************
# file: main.py
# project: Hot-Board
# author: Nils Jäggi, David Jäggli
# description: main routine
# ******************************************
import serial
import json
import sys
import time
import platform
import profile_handler
import vcp_handler as vcp



com = vcp.VirtualComPort('s', 2)

print('Ports: ', com.get_available_serial_ports())