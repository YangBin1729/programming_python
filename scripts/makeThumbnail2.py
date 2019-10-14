#!python3
# makeThumbnial2.py - A updated version of makeThumbnail.py,using parallel computing

import glob
import concurrent.futures
from makeThumbnail import make_thumbnail


with concurrent.futures.ProcessPoolExecutor() as executor:
    images = glob.glob('*.jpg')
    for im, thumbnail_file in zip(images, executor.map(make_thumbnail, images)):
        print((f'A thumbnail for {im} was saved as {thumbnail_file}'))
