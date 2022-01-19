import os
import sys
import json
import bz2
import pyDes

# Get current path and add the filename
DEFAULT_PROFILE_PATH = os.path.join(sys.path[0],'profiles.json')

class ProfileHandler():
    """
    This class handles all the parameters for the actions with the keys.

    It takes over saving and reading of properties from the xml-file and
    all functions that are executed at the pressing of a key take place here
    """

    def __init__(self, key_number: int = 12, path: str = DEFAULT_PROFILE_PATH):
        self.key_number = key_number
        self.path = path
        self.key_functions = []
        

    def load_settings(self):
        # check if a profile file exists
        try:
            with open(self.path, 'r') as settings_file:
                settings = json.load(settings_file)

        # If there is no valid profile file -> create one and fill it with the default parameters
        except FileNotFoundError:
            settings = {}
            settings["user1"] = {"name": "user1", "keys": {}}

            for i in range(11):
                settings["user1"]["keys"]["s" + str(i+1)] = {"function": "", "args": ""}

            with open(self.path, 'w') as f:
                json.dump(settings, f)
            
        return settings


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
