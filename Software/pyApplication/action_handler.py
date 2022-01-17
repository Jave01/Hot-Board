import os
import json
from pynput.keyboard import Key, Controller
import webbrowser


keyboard = Controller()

class KeyAction():
    @classmethod
    def execute_action(cls, action: str, args: str):
        """Execute the function from the key"""
        if action == "execute file":
            # try to start file on given path
            try:
                os.startfile(args)
            except FileNotFoundError:
                print(f"File at {args} not found")
                return

        elif action == "hotkey":
            # save keys separately in a list
            keys_to_press = args.split(',')
            # press each key, including special keys
            for k in keys_to_press:
                # if its a single char, its not a special key
                if len(k) == 1:
                    cls.keyboard.press(k)
                else:
                    cls.press_special_key(k)

            # release every pressed key
            for k in keys_to_press:
                if len(k) == 1:
                    cls.keyboard.release(k)
                else:
                    cls.release_special_key(k)

        elif action == "open url":
            webbrowser.open(args)

  
    @classmethod
    def load_settings(cls, path_to_file):
        try:
            with open(path_to_file, 'r') as f:
                cls.key_settings = json.load(f)

        except FileNotFoundError:
            print("File at given path was not found")


    @classmethod
    def press_special_key(cls, key):
        if key == 'Ctrl':
            cls.keyboard.press(Key.ctrl)
        elif key == 'Shift':
            cls.keyboard.press(Key.shift)
        elif key == 'Alt':
            cls.keyboard.press(Key.alt)
        elif key == 'Win':
            cls.keyboard.press(Key.cmd)
        elif key == 'F4':
            cls.keyboard.press(Key.f4)
        elif key == 'F7':
            cls.keyboard.press(Key.f7)
        elif key == 'F9':
            cls.keyboard.press(Key.f9)
        elif key == 'PlayPause':
            cls.keyboard.press(Key.media_play_pause)
        elif key == 'previous':
            cls.keyboard.press(Key.media_previous)
        elif key == 'next':
            cls.keyboard.press(Key.media_next)

    @classmethod
    def release_special_key(cls, key):
        if key == 'Ctrl':
            cls.keyboard.release(Key.ctrl)
        elif key == 'Shift':
            cls.keyboard.release(Key.shift)
        elif key == 'Alt':
            cls.keyboard.release(Key.alt)
        elif key == 'Win':
            cls.keyboard.release(Key.cmd)
        elif key == 'F4':
            cls.keyboard.release(Key.f4)
        elif key == 'F7':
            cls.keyboard.release(Key.f7)
        elif key == 'F9':
            cls.keyboard.release(Key.f9)
        elif key == 'PlayPause':
            cls.keyboard.release(Key.media_play_pause)
        elif key == 'previous':
            cls.keyboard.release(Key.media_previous)
        elif key == 'next':
            cls.keyboard.release(Key.media_next)