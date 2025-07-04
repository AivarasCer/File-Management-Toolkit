# Functions:
# File Count Analyser: Finds the folder within a directory tree that contains the highest number of files.
# Disk Space Analyser: Identifies the folder that occupies the most disk space.
# File Type Distribution Analyser: Analyses the distribution of different file types (like .txt, .jpg, .py, etc.) within a directory and its subdirectories.
# Large File Finder: Identifies the largest files within a directory tree.

import heapq
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


def file_type_dist_analyser(directory):
    """
        Analyzes the distribution of different file types within a directory and its subdirectories.

        Params:
        directory (str): Path to the directory to analyze.

        Returns:
        Counter: A Counter object containing file extensions and their counts.
    """
    base_path = Path(directory)
    file_types = Counter()

    for file in base_path.rglob('*'):
        if file.is_file():
            file_types[file.suffix] += 1

    return file_types


def large_file_finder(directory, num_files=10):
    """
        Identifies the largest files within a directory tree.

        Params:
        directory (str): Path to the directory to analyze.
        num_files (int): Number of top largest files to find.

        Returns:
        list: A list of tuples, each containing a file path and its size in bytes.
    """
    base_path = Path(directory)
    largest_files = []

    for file in base_path.rglob('*'):
        if file.is_file():
            file_size = file.stat().st_size
            if len(largest_files) < num_files:
                heapq.heappush(largest_files, (file_size, file))
            else:
                heapq.heappush(largest_files, (file_size, file))

    largest_files.sort(reverse=True, key=lambda x: x[0])
    return largest_files[:num_files]


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
            directory_path = input("Enter the path to the directory to analyse (File Count Analyser): ")
            folder, count = file_count_analyser(directory_path)
            if folder:
                print(f'The folder with the most files is: {folder} with {count} files.')
            elif directory_path == 'exit':
                print('Exiting.')
                break
            else:
                print('No files found in the given directory.')
        elif user_choice == '2':
            directory_path = input('Enter the path to the directory to analyse (Disk Space Analyser): ')
            folder, space = disk_space_analyser(directory_path)
            if folder:
                print(f'The folder occupying the most disk space is: {folder} using {space} bytes.')
            elif directory_path == 'exit':
                print('Exiting.')
                break
            else:
                print('No files found in the given directory or directory is empty.')
        elif user_choice == '3':
            directory_path = input('Enter the path to the directory to analyze (File Type Distribution): ')
            distribution = file_type_dist_analyser(directory_path)
            if distribution:
                print('File type distribution:')
                for file_type, count in distribution.items():
                    print(f" {file_type if file_type else 'No Extension'}: {count}")
            elif directory_path == 'exit':
                print('Exiting.')
                break
            else:
                print('No files found in the given directory or directory is empty.')
        elif user_choice == '4':
            directory_path = input('Enter the path to the directory to analyze (Large Files): ')
            if directory_path == 'exit':
                print('Exiting.')
                break
            num_files_to_find = int(input('How many large files to find? '))
            largest_files = large_file_finder(directory_path, num_files_to_find)
            if largest_files:
                print('Largest files found:')
                for size, file in largest_files:
                    print(f'{file}: {size} bytes.')
            else:
                print('No files found in the given directory or directory is empty.')
        elif user_choice == '5':
            print('Exiting.')
            break
        else:
            print('Invalid option. Please try again.')


if __name__ == '__main__':
    main()
