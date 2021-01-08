# ******************************************
# file: main.py
# project: Hot-Board
# author: Nils Jäggi, David Jäggli
# description: main routine
# ******************************************
import serial
import subprocess
import sys,os
from profile_handler import ProfileHandler
from vcp_handler import VirtualComPort
from console_gui import run_gui

vcp = VirtualComPort('s', 2)    # define serial protocoll -> eg. 's01' for switch 1
# profile file must be im the same dir as main
ProfileHandler = ProfileHandler(path=os.path.join(sys.path[0],'profiles.xml'))
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
                #os.system('python ' + os.path.join(sys.path[0],'main.py'))
                #os.execv(sys.executable, ['python'] + [os.path.join(sys.path[0],'main.py')])
                #os.spawnl(sys.executable, ['python'] + [os.path.join(sys.path[0],'main.py')])
                run_gui()

                #os.system('pythonw.exe ' + os.path.join(sys.path[0],'main.py'))

                # restart script
                #os.execv(sys.executable, ['python'] + [os.path.join(sys.path[0],'main.pyw')])
                os.execv(sys.executable, ['python'] + sys.argv)
                vcp.ser.flushInput() # flush serial buffer, so the pressed buttons while the gui was open, get deleted
            elif key == 's12':
                print(ProfileHandler.key_functions)
                break
            else:
                ProfileHandler.execute_action(key)
    else:
        wait_for_board()
