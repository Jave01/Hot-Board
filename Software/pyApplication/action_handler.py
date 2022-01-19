import os
from pynput.keyboard import Key, Controller
import webbrowser




class KeyAction():
    keyboard = Controller()

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
                    if not cls.press_special_key(k):
                        print("Special key not found")

            # release every pressed key
            for k in keys_to_press:
                if len(k) == 1:
                    cls.keyboard.release(k)
                else:
                    cls.release_special_key(k)

        elif action == "open url":
            webbrowser.open(args)

  
    @classmethod
    def press_special_key(cls, key) -> bool:
        if key == 'Ctrl':
            cls.keyboard.press(Key.ctrl)
            return True
        elif key == 'Shift':
            cls.keyboard.press(Key.shift)
            return True
        elif key == 'Alt':
            cls.keyboard.press(Key.alt)
            return True
        elif key == 'Win':
            cls.keyboard.press(Key.cmd)
            return True
        elif key == 'F4':
            cls.keyboard.press(Key.f4)
            return True
        elif key == 'F7':
            cls.keyboard.press(Key.f7)
            return True
        elif key == 'F9':
            cls.keyboard.press(Key.f9)
            return True
        elif key == 'PlayPause':
            cls.keyboard.press(Key.media_play_pause)
            return True
        elif key == 'previous':
            cls.keyboard.press(Key.media_previous)
            return True
        elif key == 'next':
            cls.keyboard.press(Key.media_next)
            return True
        return False

    @classmethod
    def release_special_key(cls, key) -> bool:
        if key == 'Ctrl':
            cls.keyboard.release(Key.ctrl)
            return True
        elif key == 'Shift':
            cls.keyboard.release(Key.shift)
            return True
        elif key == 'Alt':
            cls.keyboard.release(Key.alt)
            return True
        elif key == 'Win':
            cls.keyboard.release(Key.cmd)
            return True
        elif key == 'F4':
            cls.keyboard.release(Key.f4)
            return True
        elif key == 'F7':
            cls.keyboard.release(Key.f7)
            return True
        elif key == 'F9':
            cls.keyboard.release(Key.f9)
            return True
        elif key == 'PlayPause':
            cls.keyboard.release(Key.media_play_pause)
            return True
        elif key == 'previous':
            cls.keyboard.release(Key.media_previous)
            return True
        elif key == 'next':
            cls.keyboard.release(Key.media_next)
            return True
        return False