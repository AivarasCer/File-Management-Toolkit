# Duplicate File Finder:
# Script scans directories for duplicate files.
# This can help free up storage space and declutter your file system.
# The script uses hashes to find duplicates.

import hashlib
import shutil
from pathlib import Path
from collections import defaultdict


class DublicateFileFinder:

    def __init__(self, directory):
        self.directory = directory

    def generate_hash(self, file_path, hash_func=hashlib.md5):
        """ Generates a hash for a file's contents. """
        hash_obj = hash_func()
        with open(file_path, 'rb') as file:

            for chunk in iter(lambda: file.read(4096), b''):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()

    def find_duplicates(self):
        """ Finds and returns a list of duplicate files. """
        files_by_hash = defaultdict(list)
        base_path = Path(self.directory)

        for file_path in base_path.rglob('*'):
            if file_path.is_file() and not file_path.is_symlink():
                file_hash = self.generate_hash(file_path)

                files_by_hash[file_hash].append(file_path)

        return {hash_val: paths for hash_val, paths in files_by_hash.items() if len(paths) > 1}

    def delete_file(self, file_path):
        """ Deletes a file at the given path. """
        try:
            file_path.unlink()
            return True
        except Exception as e:
            print(f'Error deleting file {file_path}: {e}')
            return False

    def move_file(self, file_path, destination):
        """ Moves a file to the specified destination directory. """
        try:
            destination_path = Path(destination) / file_path.name
            shutil.move(str(file_path), str(destination_path))
            return True
        except Exception as e:
            print(f"Error moving file {file_path} to {destination}: {e}")
            return False


def main():
    directory = input("Enter the path to the directory to scan for duplicates: ")
    finder = DublicateFileFinder(directory)
    duplicates = finder.find_duplicates()

    if duplicates:
        print('Duplicate files found:')
        for hash_val, files in duplicates.items():
            print(f"Hash: {hash_val}")
            for file in files:
                print(f" - {file}")

        user_action = int(input('What do you want to do with duplicates?'
                                '\n1. Delete'
                                '\n2. Move'
                                '\n3. Exit program'
                                '\n> '))
        if user_action == 1:
            for _, files in duplicates.items():
                # Skipping the first file to keep one of the copies.
                for file_path in files[1:]:
                    finder.delete_file(file_path)
                    print('Duplicates has been deleted.')

        elif user_action == 2:
            destination = input('Enter the destination directory to move duplicates: ')
            for _, files in duplicates.items():
                for file_path in files[1:]:
                    finder.move_file(file_path, destination)
                    print('Duplicates has been moved.')

        elif user_action == 3:
            print('Exiting the program.')

    else:
        print("No duplicate files found.")


if __name__ == '__main__':
    main()
