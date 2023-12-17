# Directory Organizer
# Script that sorts files into folders based on file type, name (regex), or date.
# For instance, all .jpg files go into an 'Jpg' folder, all .docx files into a 'Docx' folder, etc.

import re
import datetime
from pathlib import Path


class DirectoryOrganiser:

    def __init__(self, directory):
        self.directory = Path(directory)

    def organise_by_type(self):
        """ Organizes files based on their type. """
        for file in self.directory.glob('*'):
            if file.is_file():
                destination_folder = self.directory / file.suffix.lstrip('.').capitalize()
                destination_folder.mkdir(exist_ok=True)

                file.rename(destination_folder / file.name)
                print(f'Moved {file.name} to {destination_folder}')

    def organise_by_name(self, pattern, folder_name):
        """ Organizes files based on a regex pattern in their names. """
        compiled_pattern = re.compile(pattern)
        destination_folder = self.directory / folder_name
        destination_folder.mkdir(exist_ok=True)

        for file in self.directory.glob('*'):
            if file.is_file() and compiled_pattern.search(file.name):
                file.rename(destination_folder / file.name)
                print(f'Moved {file.name} to {destination_folder}')

    def organise_by_date(self):
        """ Organizes files into folders based on their modification date. """
        for file in self.directory.glob('*'):
            if file.is_file():
                mod_time = datetime.datetime.fromtimestamp(file.stat().st_mtime)
                folder_name = mod_time.strftime('%Y-%m-%d')
                destination_folder = self.directory / folder_name
                destination_folder.mkdir(exist_ok=True)

                file.rename(destination_folder / file.name)
                print(f'Moved {file.name} to {destination_folder}')


def main():
    directory = input('Enter the path to the directory to organize: ')
    organiser = DirectoryOrganiser(directory)
    user_choice = int(input('Select your action:'
                            '\n1. Organise by type'
                            '\n2. Organise by name'
                            '\n3. Organise by date'
                            '\n4. Exit'
                            '\n> '))
    if user_choice == 1:
        organiser.organise_by_type()
        print('Files were successfully organised by type.')

    elif user_choice == 2:
        pattern = input('Enter the regex pattern: ')
        dir_name = input('Enter the folder name: ')
        organiser.organise_by_name(pattern, dir_name)
        print('Files were successfully organised by name.')

    elif user_choice == 3:
        organiser.organise_by_date()
        print('Files were successfully organised by date.')

    elif user_choice == 4:
        print('Exiting.')


if __name__ == "__main__":
    main()
