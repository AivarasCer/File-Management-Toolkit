# This script walks through a directory tree and archives every file except those with specified extensions.
# It allows for comprehensive archiving while excluding certain file types.
# Useful for general backups where common file types (like text and script files) need to be excluded.

import argparse as a
from pathlib import Path
import zipfile as z


def inverse_archiver(directory, exclude_extensions=None):
    """
    Archives files in a given directory, optionally excluding files with specified extensions.

    Params: directory (str): The path to the directory whose files are to be archived.
            exclude_extensions (set of str, optional): A set of file extensions to exclude from archiving.
            If None, all files are included. Defaults to None.

    Returns two elements:   1. A list of the names of all files and folders contained in the archive.
                            2. The compression efficiency, calculated as original size / compressed size.
    """
    base_path = Path(directory)
    zip_filename = base_path / 'archive.zip'
    original_size = 0

    with z.ZipFile(zip_filename, 'w', z.ZIP_DEFLATED) as zipf:
        for file_path in base_path.rglob('*'):
            if file_path.is_file() and (exclude_extensions is None or file_path.suffix not in exclude_extensions):
                zipf.write(file_path, file_path.relative_to(base_path))
                original_size += file_path.stat().st_size

    compressed_size = zip_filename.stat().st_size

    with z.ZipFile(zip_filename, 'r') as zipf:
        zip_contents = zipf.namelist()

    efficiency = original_size / compressed_size if compressed_size > 0 else 0

    return zip_contents, efficiency


def main():
    parser = a.ArgumentParser(description='Selective Extension Archiver')
    parser.add_argument('directory', type=str, help='Directory to archive')
    parser.add_argument('-ex', '--exclude', nargs='*', help='File extensions to exclude from archiving')
    args = parser.parse_args()

    contents, efficiency = inverse_archiver(args.directory, exclude_extensions=set(args.exclude) if args.exclude else None)
    print("Files in ZIP:", contents)
    print("Compression Efficiency: {:.2f}".format(efficiency))

if __name__ == "__main__":
    main()
