# Functions:
# File Count Analyser: Finds the folder within a directory tree that contains the highest number of files.
# Disk Space Analyser: Identifies the folder that occupies the most disk space.
# File Type Distribution Analyzer: Analyses the distribution of different file types (like .txt, .jpg, .py, etc.) within a directory and its subdirectories.
# Large File Finder: Identifies the largest files within a directory tree.

import os
from pathlib import Path
from collections import Counter, defaultdict


def file_count_analyser(directory):
    """
        Analyzes the given directory to find the folder with the highest number of files.

        Params:
        directory (str): Path to the directory to analyze.

        Returns:
        tuple: A tuple containing the path to the folder with the most files and the file count.
    """
    base_path = Path(directory)
    file_counts = Counter()

    for file in base_path.rglob('*'):
        if file.is_file():
            file_counts[file.parent] += 1

    most_common = file_counts.most_common(1)
    return most_common[0] if most_common else (None, 0)


def disk_space_analyser(directory):
    """
        Analyzes the given directory to find the folder that occupies the most disk space.

        Params:
        directory (str): Path to the directory to analyze.

        Returns:
        tuple: A tuple containing the path to the folder occupying the most disk space and the total size in bytes.
    """
    base_path = Path(directory)
    space_usage = defaultdict(int)

    for file in base_path.rglob('*'):
        if file.is_file():
            space_usage[file.parent] += file.stat().st_size

    if not space_usage:
        return None, 0

    max_space_folder = max(space_usage, key=space_usage.get)
    max_space = space_usage[max_space_folder]
    return max_space_folder, max_space


def file_type_dist_analyser():
    pass


def large_type_finder():
    pass


def main():
    user_choice = input('Select function:'
                        '\n1. File Count Analyser'
                        '\n2. Disk Space Analyser'
                        '\n3. File Type Distribution Analyser'
                        '\n4. Large File Finder'
                        '\n5. Exit'
                        '\n> ')
    while True:
        if user_choice == '1':
            directory_path = input("Enter the path to the directory to analyse: ")
            folder, count = file_count_analyser(directory_path)
            if folder:
                print(f'The folder with the most files is: {folder} with {count} files.')
            elif directory_path == 'exit':
                print("Exiting.")
                break
            else:
                print("No files found in the given directory.")
        elif user_choice == '2':
            directory_path = input("Enter the path to the directory to analyse: ")
            folder, space = disk_space_analyser(directory_path)
            if folder:
                print(f'The folder occupying the most disk space is: {folder} using {space} bytes.')
            elif directory_path == 'exit':
                print("Exiting.")
                break
            else:
                print("No files found in the given directory or directory is empty.")
        elif user_choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
