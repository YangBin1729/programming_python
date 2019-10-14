#!python3
# makeThumbnail.py - Creates thumbnails of given images

from PIL import Image
import os
import glob


def make_thumbnail(filename):
    basename, file_extension = os.path.splitext(filename)
    thumbnail_name = f'{basename}_thumbnail{file_extension}'

    image = Image.open(filename)
    image.thumbnail((128, 128))
    image.save(thumbnail_name, 'JPEG')

    return thumbnail_name


for im in glob.glob('*.jpg'):
    thumbnail_file = make_thumbnail(im)
    print(f'A thumbnail for {im} was saved as {thumbnail_file}')