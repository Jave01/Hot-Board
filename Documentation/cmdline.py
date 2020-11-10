# https://github.com/CITGuru/PyInquirer/blob/master/examples/input.py

from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint


style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

print("┌────────────┐")
print("│ 1  2  3  4 │")
print("│ 5  6  7  8 │")
print("│ 9 10 11 12 │")
print("└────────────┘")


sw_actions = [
    {
        'type': 'list',
        'message': 'Select action',
        'name': 'action',
        'choices': [
            {'name': 'run application'},
            {'name': 'lock Windows'},
            {'name': 'open url'},
            {'name': '←'}
        ]
    }
]

sw_select = [
    {
        'type': 'list',
        'message': 'Select action',
        'name': 'action',
        'choices': [
            {'name': 'Switch 1'},
            {'name': 'Switch 2'},
            {'name': 'Switch 3'},
            {'name': 'Switch 4'},
            {'name': 'Switch 5'},
            {'name': 'Switch 6'},
            {'name': 'Switch 7'},
            {'name': 'Switch 8'},
            {'name': 'Switch 9'},
            {'name': 'Switch 10'},
            {'name': 'Switch 11'},
            {'name': 'Switch 12'},
            {'name': '←'}
        ]
    }
]

path_taker = [
    {
        'type': 'input',
        'message': 'input the desired path:',
        'name': 'action'
    }
]

answers = prompt(sw_select, style=style)
answers = prompt(sw_actions, style=style)
answers = prompt(path_taker, style=style)
pprint(answers)