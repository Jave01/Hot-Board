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



def wait_for_board():
    known_ports = []
    while not vcp.ser.isOpen():
        # Get all ports connected to a STM
        ports = vcp.search_board()
        #Check if anything changed
        if ports != known_ports:
            known_ports = ports
            # Try to start the hotboard
            if vcp.start_hot_board():
                break
            else:
                continue

while True:
    if vcp.ser.isOpen():
        key = vcp.check_switch_state()
        if key != '':
            print(key)
            if key == 's11':
                break
        ProfileHandler.execute_action(key)
    else:
        wait_for_board()