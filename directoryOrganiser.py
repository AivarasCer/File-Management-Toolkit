# Directory Organizer
# Script that sorts files into folders based on file type, name, or date.
# For instance, all .jpg files go into an 'Images' folder, all .docx files into a 'Documents' folder, etc.

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

    def organise_by_name(self):
        pass

    def organise_by_date(self):
        pass


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
        organiser.organise_by_name()
        print('Files were successfully organised by name.')

    elif user_choice == 3:
        organiser.organise_by_date()
        print('Files were successfully organised by date.')

    elif user_choice == 4:
        print('Exiting')


if __name__ == "__main__":
    main()
