# Duplicate File Finder:
# Script scans directories for duplicate files.
# This can help free up storage space and declutter your file system.
# The script uses hashes to find duplicates.

import hashlib
from pathlib import Path
from collections import defaultdict


class DublicateFileFinder:

    def __init__(self, directory):
        self.directory = directory

    def generate_hash(self, file_path, hash_func=hashlib.md5):
        """
            Generates a hash for a file's contents.
        """
        hash_obj = hash_func()
        with open(file_path, 'rb') as file:

            for chunk in iter(lambda: file.read(4096), b''):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()

    def find_duplicates(self):
        """
            Finds and returns a list of duplicate files.
        """
        files_by_hash = defaultdict(list)
        base_path = Path(self.directory)

        for file_path in base_path.rglob('*'):
            if file_path.is_file():
                file_hash = self.generate_hash(file_path)

                files_by_hash[file_hash].append(file_path)

        return {hash_val: paths for hash_val, paths in files_by_hash.items() if len(paths) > 1}


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
    else:
        print("No duplicate files found.")


if __name__ == '__main__':
    main()
