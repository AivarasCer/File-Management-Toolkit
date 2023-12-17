# Bulk Image Resizer
# A script to resize a batch of images to a specified size.
# This is useful for web development, where you might need images of consistent sizes.

from pathlib import Path
from PIL import Image


def image_resizer(directory, size):
    base_path = Path(directory)

    for img_path in base_path.glob('*.[jp][pn]g'):
        with Image.open(img_path) as img:
            resized_img = img.resize(size, Image.Resampling.LANCZOS)

            resized_img.save(img_path)
            print(f'Resized and saved {img_path}')


def main():
    directory = input('Enter the path to the image directory: ')
    width = int(input('Enter the target width: '))
    height = int(input('Enter the target height: '))
    image_resizer(directory, (width, height))

if __name__ == "__main__":
    main()
