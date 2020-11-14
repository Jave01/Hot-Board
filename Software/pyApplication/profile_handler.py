import os
import xml.etree.ElementTree as ET
from pynput.keyboard import Key, Controller
import webbrowser


class ProfileHandler():
    def __init__(self, key_number: int = 12, path: str = 'profiles.xml'):
        self.active_user = 'user1'
        self.key_number = key_number
        self.path = path
        self.keyboard = Controller()
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
        pass

    def export_profile(self):
        pass

    def import_profile(self):
        pass

    def change_user(self, new_user: str):
        for user in self.root:
            if user == new_user:
                self.active_user = new_user
                print('new user set')
                return
        print('No valid user found')




    def change_action(self, key: str, new_action: str, action_info=''):
        """
        Change the command which will be executed on press of any key
        Hand over some additional info if needed like a path.
        :return: None
        """
        for u in self.root.iter(self.active_user):
            print('Found user')
            for k in u:
                if k.get('name') == key:
                    print('Found Key')
                    k.set('function', new_action)
                    k.set('additional_info', action_info)
                    self.tree.write(self.path)
                    print('wrote info')
                    break
            else:
                continue
            break

    def execute_action(self, key):
        """Searches the xml file for the given key and executes the action"""
        for k in self.root.iter('key'):
            if k.get('name') == key:
                function = k.get('function')
                info = k.get('additional_info')
                if function != '':
                    if function == 'start program':
                        try:
                            os.startfile(info)
                        except FileNotFoundError:
                            print('File on path:\n' + info + '\nnot Found')
                    elif function == 'hotkey':
                        keys_to_press = info.split(',')
                        for k in keys_to_press:
                            if len(k) == 1:
                                self.keyboard.press(k)
                            else:
                                self.press_special_key(k)

                        for k in keys_to_press:
                            if len(k) == 1:
                                self.keyboard.release(k)
                            else:
                                self.release_special_key(k)

                    elif function == 'url':
                        webbrowser.open(info)

                    else:
                        break
        return

    def press_special_key(self, key):
        if key == 'Ctrl':
            self.keyboard.press(Key.ctrl)
        elif key == 'Shift':
            self.keyboard.press(Key.shift)
        elif key == 'Alt':
            self.keyboard.press(Key.alt)
        elif key == 'Win':
            self.keyboard.press(Key.cmd)
        elif key == 'f4':
            self.keyboard.press(Key.f4)
        elif key == 'f7':
            self.keyboard.press(Key.f7)
        elif key == 'f9':
            self.keyboard.press(Key.f9)
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
        elif key == 'f4':
            self.keyboard.release(Key.f4)
        elif key == 'f7':
            self.keyboard.release(Key.f7)
        elif key == 'f9':
            self.keyboard.release(Key.f9)
        return


#region old crappy code

#Note: The name of this region doesnt mean that my new code is better, I just dont like the one below

# while True:
#     key = input('Enter valid Key Number: ')
#     # Check if key number is valid
#     if int(key) <= self.key_number and int(key) > 0:
#         break
#     else:
#         print('Key number must be between 1 and', self.key_number)
#
# print('Enter new action, available actions are:')
# for action in self.hotkey_actions:
#     print('- ' + action)
#
# while True:
#     new_action = input('New Action: ')
#     if new_action == 'exit':
#         print('interrupted')
#         return
#
#     if new_action in self.hotkey_actions:
#         new_additional_info = input('Enter additional info (leave blank if not needed): ')
#
#         for k in self.root.iter('key'):
#             if k.get('name') == 's' + str(int(key) - 1):
#                 k.set('function', new_action)
#                 k.set('additional_info', new_additional_info)
#                 self.tree.write('settings\\profiles.xml')
#                 print('new action set')
#                 break
#         else:
#             print('something went wrong')
#     else:
#         print('not valid, enter "exit" to interrupt the process')
# return


# test = ProfileHandler()
# test.change_action('user2', 's4', 'action nr.4', 'some info')