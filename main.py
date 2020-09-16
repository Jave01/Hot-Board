# ******************************************
# file: main.py
# project: Hot-Board
# ******************************************
import vcp_handler
import event_handler
import serial
import json
import sys
#ser = serial.Serial()
#serial.Timeout = 0
#ser.read()

vcp = vcp_handler.vcp_reader()
print(vcp.get_available_serial_ports())

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)

#s.print()
