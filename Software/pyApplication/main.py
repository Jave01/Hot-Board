# ******************************************
# file: main.py
# project: Hot-Board
# author: Nils Jäggi, David Jäggli
# description: main routine
# ******************************************
import serial
from profile_handler import ProfileHandler
from vcp_handler import VirtualComPort

vcp = VirtualComPort('s', 2)
ProfileHandler = ProfileHandler()

vcp.start_hot_board()

while True:
    key = vcp.check_switch_state()
    if key != '':
        print(key)
        if key == 's11':
            break
    ProfileHandler.execute_action(key)