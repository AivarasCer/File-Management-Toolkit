# Batch File Renamer
# Script that automatically renames files in a directory based on certain criteria, like date, file type, or a custom naming scheme.
# This can be particularly useful for organizing photos, documents, or other media.

import datetime
from pathlib import Path


class BatchFileRenamer:

    def __init__(self, directory, name='renamed'):
        self.directory = directory
        self.name = name

    def file_type_renamer(self, extension):
        """
            Renames files in the directory based on their file type (extension).
        """
        base_path = Path(self.directory)
        count = 1

        for file in base_path.rglob('*'):
            if file.is_file() and file.suffix == extension:
                new_name = f'{self.name}_{count:03}{extension}'

                new_file_path = file.parent / new_name

                # Check if file with new name already exists
                if not new_file_path.exists():
                    file.rename(new_file_path)
                    count += 1
                else:
                    print(f'File {new_file_path} already exists. Skipping.')

    def file_date_renamer(self, date_format='%Y%m%d'):
        """
            Renames files in the directory based on their creation/modification date.
            Logic:
                - Traverse the directory.
                - For each file, retrieve its creation/modification date.
                - Rename the file incorporating the date in the specified format.
        """
        base_path = Path(self.directory)
        count = 1

        for file in base_path.rglob('*'):
            if file.is_file():
                mod_time = datetime.datetime.fromtimestamp(file.stat().st_mtime)
                formatted_date = mod_time.strftime(date_format)

                new_name = f'{self.name}_{formatted_date}_{count:03}{file.suffix}'
                new_file_path = file.parent / new_name

                if not new_file_path.exists():
                    file.rename(new_file_path)
                    count += 1
                else:
                    print(f'File {new_file_path} already exists. Skipping.')

    def custom_renamer(self):
        """
            Renames files in the directory based on a custom naming pattern.
            Logic:
                - Traverse the directory.
                - Rename each file according to the custom pattern provided.
                - The pattern might include sequence numbers, user-defined strings, etc.
        """
        pass


def main():
    while True:
        user_choice = int(input('Select function:'
                                '\n1. Rename by file type'
                                '\n4. Exit'
                                '\n> '))

        if user_choice == 1:
            directory_path = input('Enter the path to the directory: ')
            extension = input('Enter the desired file extension (e.g. .txt): ')
            base_name = input('Enter the base name for renaming: ')

            renamer = BatchFileRenamer(directory_path, base_name)
            renamer.file_type_renamer(extension)
            print('Renaming complete.')
        elif user_choice == 4:
            print('Exiting the program.')
            break
        else:
            print('Invalid input. Please try again.')

if __name__ == '__main__':
    main()
