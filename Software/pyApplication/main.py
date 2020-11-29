# ******************************************
# file: main.py
# project: Hot-Board
# author: Nils Jäggi, David Jäggli
# description: main routine
# ******************************************
import serial
import subprocess
import sys
from profile_handler import ProfileHandler
from vcp_handler import VirtualComPort

vcp = VirtualComPort('s', 2)    # define serial protocoll -> eg. 's01' for switch 1
ProfileHandler = ProfileHandler()
ProfileHandler.reload_actions()

def wait_for_board():
    known_ports = []
    while not vcp.ser.isOpen():
        # Get all ports connected to a STM
        ports = vcp.search_board()
        # Check if anything changed
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
        if key != '':   # if a key got pressed
            print(key)
            if key == 's0':
                subprocess.Popen([sys.executable, 'console_gui.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
                #subprocess.Popen(r"cmd", creationflags=subprocess.CREATE_NEW_CONSOLE)
                #subprocess.Popen("python console_gui.py 1", shell=True)
                #vcp.get_buffer_value() # flush serial buffer, so the pressed buttons while the gui was open, get deleted
            elif key == 's11':
                break
            else:
                ProfileHandler.execute_action(key)
    else:
        wait_for_board()
