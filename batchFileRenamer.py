# Batch File Renamer
# Script that automatically renames files in a directory based on certain criteria, like date, file type, or a custom naming scheme.
# This can be particularly useful for organizing photos, documents, or other media.

from pathlib import Path


class BatchFileRenamer:

    def file_type_renamer(self, directory, extension):
        """
            Renames files in the directory based on their file type (extension).
            Logic:
                - Traverse the directory.
                - For each file matching the specified file type, rename it according to a specific pattern.
        """
        # base_path = Path(directory)
        #
        # for file in base_path.rglob('*'):
        #     if file.is_file() and file.suffix in extension:

        pass

    def file_date_renamer(self, directory, date):
        """
            Renames files in the directory based on their creation/modification date.
            Logic:
                - Traverse the directory.
                - For each file, retrieve its creation/modification date.
                - Rename the file incorporating the date in the specified format.
        """
        pass

    def custom_renamer(self, directory, file_type):
        """
            Renames files in the directory based on a custom naming pattern.
            Logic:
                - Traverse the directory.
                - Rename each file according to the custom pattern provided.
                - The pattern might include sequence numbers, user-defined strings, etc.
        """
        pass


def main():
    pass

if __name__ == '__main__':
    main()
