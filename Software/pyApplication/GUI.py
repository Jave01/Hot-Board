from PyInquirer import prompt, Separator
from profile_handler import ProfileHandler

# users = []       not available right now
keys = []
actions = ['Execute File', 'Hotkey', 'Open URL']

ProfileHandler = ProfileHandler()

for i in range(12):
    keys.append('s' + str(i))


basic_questions = [
    {
        'type': 'list',
        'name': 'menu',
        'message': 'What do you want to do?',
        'choices': [
            'Change key action',
            # 'Change User Profile'
            'exit'
        ]
    }
]

key_questions = [
    {
        'type': 'list',
        'name': 'key_select',
        'message': 'Select a key',
        'choices': keys
    },
    {
        'type': 'list',
        'name': 'action_select',
        'message': 'Select an action',
        'choices': actions
    }
]

hotkey_question = [
    {
        'type': 'checkbox',
        'name': 'select_special_keys',
        'message': 'Select special keys',
        'choices': [
            {
                'name': 'Ctrl'
            },
            {
                'name': 'Shift'
            },
            {
                'name': 'Alt'
            },
{
                'name': 'Win'
            },
            {
                'name': 'F4'
            },
            {
                'name': 'F7'
            },
            {
                'name': 'F9'
            },
            Separator(' -- Media Actions --'),
            {
                'name': 'PlayPause'
            },
            {
                'name': 'next'
            },
            {
                'name': 'previous'
            },
        ]
    },
    {
        'type': 'input',
        'name': 'select_normal_keys',
        'message': 'Enter normal keys (a-z), leave blank if not needed',
    }
]

path_question = [
    {
        'type': 'input',
        'name': 'path',
        'message': 'Enter path to file',
    }
]

def list_to_hotkey(hotkey_list: list):
    """ converts a list into a readable format for the profile handler.

        The final format is a string with the arguments split by commas"""
    final_string = ''
    for key in hotkey_list:
        final_string += (key + ',')

    return final_string[:-1]


while True:
    menu = prompt(basic_questions)
    if menu['menu'] == 'Change key action':
        # get the needed values from the user
        key_info = prompt(key_questions)
        selected_key = key_info['key_select']
        selected_action = key_info['action_select']

        if selected_action == 'Hotkey':
            # get keys from user
            hotkey_keys = prompt(hotkey_question)
            # store keys in a list
            special_keys = hotkey_keys['select_special_keys']
            normal_keys = list(hotkey_keys['select_normal_keys'])
            # convert the list and change the action
            hotkey_str = list_to_hotkey(special_keys + normal_keys)
            print(selected_action.lower())
            ProfileHandler.change_action(selected_key, selected_action.lower(), hotkey_str)

        elif selected_action == 'Execute File':
            path = prompt(path_question)
            path_str = path['path']
            ProfileHandler.change_action(selected_key, selected_action.lower(), path_str)

    elif menu['menu'] == 'exit':
        break
