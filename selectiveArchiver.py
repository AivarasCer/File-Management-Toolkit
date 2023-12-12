# This script navigates through a directory tree and archives only files with specified extensions.
# It's a targeted approach for archiving, letting you focus on specific file types while excluding others.
# Ideal for backing up source code, documents, or any specific file types while ignoring others.

import zipfile as z
import argparse as a
from pathlib import Path


def selective_archiver(directory, extensions):
    """
    Archives files with specified extensions in a given directory.

    Parameters:
    directory (Path): Path object pointing to the target directory.
    extensions (list of str): List of file extensions to include in the archive.
    """
    base_path = Path(directory)
    zip_filename = base_path / 'selective_archive.zip'
    original_size = 0

    with z.ZipFile(zip_filename, 'w', z.ZIP_DEFLATED) as zipf:
        for file_path in base_path.rglob('*'):
            if file_path.is_file() and file_path.suffix in extensions:
                zipf.write(file_path, file_path.relative_to(base_path))
                original_size += file_path.stat().st_size

    compressed_size = zip_filename.stat().st_size

    with z.ZipFile(zip_filename, 'r') as zipf:
        zip_contents = zipf.namelist()

    efficiency = original_size / compressed_size / compressed_size if compressed_size > 0 else 0

    print(f'Archive created at: {zip_filename}')
    return zip_contents, efficiency


def main():
    parser = a.ArgumentParser(description='Selective Extension Archiver')
    parser.add_argument('directory', type=str, help='Directory to search files in')
    parser.add_argument('-zip', '--extensions', nargs='+', required=True, help='File extensions to include in the archive (e.g., .txt .py)')
    args = parser.parse_args()

    # Convert the directory string to a Path object
    directory_path = Path(args.directory)

    # Ensure the directory exists
    if not directory_path.exists() or not directory_path.is_dir():
        raise ValueError(f"Invalid directory: {args.directory}")

    # Call the selective archive function
    selective_archiver(directory_path, args.extensions)


if __name__ == "__main__":
    main()
