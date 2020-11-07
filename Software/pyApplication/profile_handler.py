import os
import xml.etree.ElementTree as ET



class ProfileHandler():
    def __init__(self, key_number: int):
        self.key_number = key_number
        self.hotkey_actions = ['start program', 'enter hotkey']
        # check if a profile file exists
        try:
            with open('settings\\profiles.xml', 'r') as profiles:
                self.tree = ET.parse('settings\\profiles.xml')

        # If there is no valid profile file -> create one and fill it with the default parameters
        except FileNotFoundError:
            setting_data = ET.Element('Settings')
            users = ET.SubElement(setting_data, 'users')
            user1 = ET.SubElement(users, 'user1')
            keys = ET.SubElement(user1, 'keys')
            for i in range(self.key_number):
                ET.SubElement(keys, 'key', name='s' + str(i), function='', additional_info='')

            self.tree = ET.ElementTree(setting_data)
            self.tree.write('settings\\profiles.xml')

        self.root = self.tree.getroot()
        print(self.root.tag)
        pass

    def export_profile(self):
        pass

    def import_profile(self):
        pass

    def change_action(self):
        """ Change the command which will be executed on press of any key"""
        while True:
            key = input('Enter valid Key Number: ')
            # Check if key number is valid
            if int(key) <= self.key_number and int(key) > 0:
                break
            else:
                print('Key number must be between 1 and', self.key_number)

        print('Enter new action, available actions are:')
        for action in self.hotkey_actions:
            print('- ' + action)

        while True:
            new_action = input('New Action: ')
            if new_action == 'exit':
                print('interrupted')
                return

            if new_action in self.hotkey_actions:
                new_additional_info = input('Enter additional info (leave blank if not needed): ')

                for k in self.root.iter('key'):
                    if k.get('name') == 's' + str(int(key) - 1):
                        k.set('function', new_action)
                        k.set('additional_info', new_additional_info)
                        self.tree.write('settings\\profiles.xml')
                        print('new action set')
                        break
                else:
                    print('something went wrong')
            else:
                print('not valid, enter "exit" to interrupt the process')
        return



