# ******************************************
# file: main.py
# project: Hot-Board
# author: Nils Jäggi, David Jäggli
# description: main routine
# ******************************************
import vcp_handler
#import profile_handler
import serial
import json
import sys
import time

boi = vcp_handler.VirtualComPort('s',2)
boi.start_hot_board("COM3",115200)
while True:
    state = boi.check_switch_state()
    if state != -1:
        print(state)