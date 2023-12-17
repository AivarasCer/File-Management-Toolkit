# Metadata Editor
# A script that can view or remove exif data from jpg files.

import piexif
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS


class MetadataEditor:

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def view_exif(self):
        if self.file_path.suffix.lower() in ['.jpg', '.jpeg']:
            with Image.open(self.file_path) as img:
                exif_data = img.info.get('exif')
                if not exif_data:
                    print('No EXIF data found.')
                    return

                try:
                    exif_dict = piexif.load(exif_data)
                    for ifd in exif_dict:
                        print(f"IFD: {ifd}")
                        if exif_dict[ifd]:
                            for tag in exif_dict[ifd]:
                                tag_name = TAGS.get(tag, tag)
                                value = exif_dict[ifd][tag]
                                print(f"  {tag_name}: {value}")
                    else:
                        print(f"  No data found in {ifd}")

                except Exception as e:
                    print(f"Error reading EXIF data: {e}")
        else:
            print('File format not supported for EXIF viewing.')

    def remove_exif(self):
        if self.file_path.suffix.lower() in ['.jpg', '.jpeg']:
            piexif.remove(self.file_path.as_posix())
            print(f'Removed EXIF data from {self.file_path}')
        else:
            print('File format not supported for EXIF removal.')


def main():
    file_path = input('Enter the path of the JPEG file: ')
    editor = MetadataEditor(file_path)

    while True:
        user_action = int(input('Choose action:'
                                '\n1. View EXIF data'
                                '\n2. Remove EXIF data'
                                '\n3. Exit'
                                '\n> '))

        if user_action == 1:
            editor.view_exif()

        elif user_action == 2:
            editor.remove_exif()

        elif user_action == 3:
            print('Exiting.')
            break

if __name__ == "__main__":
    main()
