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
from profile_handler import ProfileHandler
import vcp_handler as vcp

command_list = [
    ['h', 'shows available commands'],
    ['help', 'Shows available commands'],
    ['export profile', 'currently not available'],
    ['import profile', 'currently not available'],
    ['change action', 'change the action which will be executed on press'],
    ['exit', 'exit program']]



entered_command = 0
ProfileHandler = ProfileHandler(12)


def command_exists(command_check: str) -> bool:
    """
    Returns True or False if the entered command is available

    :param command_check: command to check
    :return: bool
    """
    for command_arr in command_list:
        if command_arr[0] == command_check:
            return True
    else:
        return False



while True:
    entered_command = input('Enter a Command, type "h" for help: ')
    if command_exists(entered_command):
        if entered_command == 'exit':
            print('exit program')
            break

        elif entered_command == 'h' or entered_command == 'help':
            print('Available commands:')
            for command_arr in command_list:
                print('- ' + command_arr[0] + '\n\tDescription: ' + command_arr[1])

        elif entered_command == 'change action':
            ProfileHandler.change_action()


    else:
        print('not a valid command')


