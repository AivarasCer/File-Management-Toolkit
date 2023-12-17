# Directory Organizer
# Script that sorts files into folders based on file type, name, or date.
# For instance, all .jpg files go into an 'Images' folder, all .docx files into a 'Documents' folder, etc.

from pathlib import Path


class DirectoryOrganiser:

    def __init__(self, directory):
        self.directory = Path(directory)

    def organise_by_type(self):
        pass

    def organise_by_name(self):
        pass

    def organise_by_date(self):
        pass


def main():
    directory = input('Enter the path to the directory to organize: ')
    organiser = DirectoryOrganiser(directory)

if __name__ == "__main__":
    main()
