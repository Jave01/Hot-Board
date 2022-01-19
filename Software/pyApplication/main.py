# ******************************************
# file: main.py
# project: Hot-Board
# author: Nils Jäggi, David Jäggli
# description: main routine
# ******************************************
import asyncio
from settings_handler import ProfileHandler
from vcp_handler import ConnectionHandler
from action_handler import KeyAction
import time

vcp = ConnectionHandler()    # define serial protocoll -> eg. 's01' for switch 1
# profile file must be im the same dir as main
profile_handler = ProfileHandler()


def main():
    active_user = "user1"
    key_settings = profile_handler.load_settings()
    
    while True:
        if vcp.ser.isOpen():
            key = vcp.check_switch_state()
            if key != '':   # if a key got pressed
                print(key)
                if key == 's0':
                    break
                    # run_gui()
                    # key_settings = profile_handler.load_settings()
                    # restart script
                    # #os.execv(sys.executable, ['python'] + [os.path.join(sys.path[0],'main.pyw')])
                    # os.execv(sys.executable, ['python'] + sys.argv)
                    # vcp.ser.flushInput() # flush serial buffer, so the pressed buttons while the gui was open, get deleted
                else:
                    key_action = key_settings[active_user]["keys"][key]["function"] 
                    args = key_settings[active_user]["keys"][key]["args"] 
                    KeyAction.execute_action(key_action, args)
        else:
            # wait for board to connect 
            while not vcp.ser.isOpen():
                vcp.connect_to_board()
                time.sleep(0.5)

if __name__ == "__main__":
    main()