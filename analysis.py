# Functions:
# File Count Analyzer: Finds the folder within a directory tree that contains the highest number of files.
# Disk Space Analyzer: Identifies the folder that occupies the most disk space.
# File Type Distribution Analyzer: Analyzes the distribution of different file types (like .txt, .jpg, .py, etc.) within a directory and its subdirectories.
# Large File Finder: Identifies the largest files within a directory tree.

import os
from pathlib import Path
from collections import Counter


def file_count_analyzer(directory):
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


def main():
    user_choice = input('Select function:'
                        '\n1. File Count Analyzer'
                        '\n2. Exit'
                        '\n> ')
    while True:
        if user_choice == '1':
            directory_path = input("Enter the path to the directory to analyze: ")
            folder, count = file_count_analyzer(directory_path)
            if folder:
                print(f'The folder with the most files is: {folder} with {count} files.')
            else:
                print("No files found in the given directory.")
        elif user_choice == '2':
            print("Exiting.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
