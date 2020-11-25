import os
import xml.etree.ElementTree as ET
from pynput.keyboard import Key, Controller
import webbrowser
import bz2
import pyDes

class ProfileHandler():
    """
    This class handles all the parameters for the actions with the keys.

    It takes over saving and reading of properties from the xml-file and
    all functions that are executed at the pressing of a key take place here
    """

    def __init__(self, key_number: int = 12, path: str = 'profiles.xml'):
        self.active_user = 'user1'
        self.key_number = key_number
        self.path = path
        self.keyboard = Controller()
        self.key_functions = []
        # check if a profile file exists
        try:
            with open(self.path, 'r') as profiles:
                self.tree = ET.parse(self.path)

        # If there is no valid profile file -> create one and fill it with the default parameters
        except FileNotFoundError:
            settings_data = ET.Element('Settings')
            users = ET.SubElement(settings_data, 'users')
            user = ET.SubElement(users, 'user', name='user1')
            for i in range(self.key_number):
                ET.SubElement(user, 'key', name='s' + str(i), function='', additional_info='')

            self.tree = ET.ElementTree(settings_data)
            self.tree.write(self.path)

        self.root = self.tree.getroot()
        self.reload_actions()

        with open('key.txt', 'w'):
            pass



    def reload_actions(self):
        """ Reload the actions from the xml file into the list"""
        key_attributes = []
        self.key_functions = []
        for k in self.root.iter('key'):
            key_attributes = k.get('name'), k.get('function'), k.get('additional_info')
            self.key_functions.append(list(key_attributes))


    def save_properties(self):
        """Takes the information from the list and saves it into the xml file"""

        for i, k in enumerate(self.root.iter('key'), 0):
            # update every property from the list into the xml file
            k.set('function', self.key_functions[i][1])
            k.set('additional_info', self.key_functions[i][2])

        self.tree.write(self.path)


    def change_action(self, key: str, new_action: str, action_info=''):
        """ Change action in list and save it"""

        # search list for given key
        for k in self.key_functions:
            # compare names
            if k[0] == key:
                # set new parameters
                k[1] = new_action
                k[2] = action_info
                print('actions set')
                break

        self.save_properties()
        self.reload_actions()


    def execute_action(self, key: str):
        """Execute the function from the key"""
        # search list for key by names
        for k in self.key_functions:
            if k[0] == key:
                # get action and execute it
                function = k[1]
                info = k[2]
                if function != '':
                    if function == 'execute file':
                        # try to start the file on saved path
                        try:
                            os.startfile(info)
                        except FileNotFoundError:
                            print('File on path:\n' + info + '\nnot Found')

                    elif function == 'hotkey':
                        # save keys separately in a list
                        keys_to_press = info.split(',')
                        # press each key, includes special keys
                        for k in keys_to_press:
                            # if its a single char, its not a special key
                            if len(k) == 1:
                                self.keyboard.press(k)
                            else:
                                self.press_special_key(k)

                        # release every pressed key
                        for k in keys_to_press:
                            if len(k) == 1:
                                self.keyboard.release(k)
                            else:
                                self.release_special_key(k)

                    elif function == 'open url':
                        webbrowser.open(info)

                break


    def press_special_key(self, key):
        if key == 'Ctrl':
            self.keyboard.press(Key.ctrl)
        elif key == 'Shift':
            self.keyboard.press(Key.shift)
        elif key == 'Alt':
            self.keyboard.press(Key.alt)
        elif key == 'Win':
            self.keyboard.press(Key.cmd)
        elif key == 'F4':
            self.keyboard.press(Key.f4)
        elif key == 'F7':
            self.keyboard.press(Key.f7)
        elif key == 'F9':
            self.keyboard.press(Key.f9)
        elif key == 'PlayPause':
            self.keyboard.press(Key.media_play_pause)
        elif key == 'previous':
            self.keyboard.press(Key.media_previous)
        elif key == 'next':
            self.keyboard.press(Key.media_next)
        return


    def release_special_key(self, key):
        if key == 'Ctrl':
            self.keyboard.release(Key.ctrl)
        elif key == 'Shift':
            self.keyboard.release(Key.shift)
        elif key == 'Alt':
            self.keyboard.release(Key.alt)
        elif key == 'Win':
            self.keyboard.release(Key.cmd)
        elif key == 'F4':
            self.keyboard.release(Key.f4)
        elif key == 'F7':
            self.keyboard.release(Key.f7)
        elif key == 'F9':
            self.keyboard.release(Key.f9)
        elif key == 'PlayPause':
            self.keyboard.release(Key.media_play_pause)
        elif key == 'previous':
            self.keyboard.release(Key.media_previous)
        elif key == 'next':
            self.keyboard.release(Key.media_next)
        return