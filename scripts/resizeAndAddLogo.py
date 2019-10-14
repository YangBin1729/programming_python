#!python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit in a 300×300 square,
# and adds catlogo.png to the lower_right-corner.

import os
from PIL import Image

square_fit_size = 300
logo_filename = 'catlogo.png'

logoIm = Image.open(logo_filename)
logoWidth, logoHeight = logoIm.size
for filename in os.listdir('.'):
    if not filename.endswith('.png') or not filename.endswith('.jpg') or filename == logo_filename:
        continue
    im = Image.open(filename)
    width, height = im.size
    if width > square_fit_size and height > square_fit_size:
        if width >height:
            height = int((square_fit_size/width)*height)
            width = square_fit_size
        else:
            width = int((square_fit_size/height)*width)
            height = square_fit_size
        print('Resizeing %s...'%filename)
        im = im.resize((width, height))

        print('Adding logo to %s...'%logo_filename)
        im.paste(logoIm, (width-logoWidth, height-logoHeight),logoIm)
        im.save(os.path.join('withLogo',filename))