# Multi Clipboard
# This program saves each piece of clipboard text under a keyword.
# This text can later be loaded to the clipboard again.
# py mc.py save <keyword> - to save
# py mc.py load <keyword> - to load
# py mc.py load <keyword> - to list keywords

import shelve
import pyperclip
import sys


class MultiClip:

    def __init__(self, db_path='clipboard_items.db'):
        self.db_path = db_path

    def save_to_cliboard(self, key):
        with shelve.open(self.db_path) as storage:
            storage[key] = pyperclip.paste()
            print(f"Text saved under key '{key}'.")

    def load_from_clipboard(self, key):
        with shelve.open(self.db_path) as storage:
            text = storage.get(key, None)
            if text:
                pyperclip.copy(text)
                print(f"Text under key '{key}' copied to clipboard.")
            else:
                print(f"No text found for key '{key}'.")

    def list_clipboard_keys(self):
        pass


def main():
    clipboarder = MultiClip()

    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        clipboarder.save_to_cliboard(sys.argv[2])

    elif len(sys.argv) == 3 and sys.argv[1].lower() == 'load':
        clipboarder.load_from_clipboard(sys.argv[2])


if __name__ == "__main__":
    main()
