import json

settings = {'Key1': 'val1', 'Key2': 'Val2'}
config = 0

with open('settings.json', 'r') as f:
    config = json.load(f)


config['Key2'] = 3

with open('settings.json', 'w+') as f_settings:
    json.dump(config, f_settings)