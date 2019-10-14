#!python3
# viewer-thumbs-grid.py - 使缩略图呈网格状排列

import os
import sys
import math
from tkinter import *
from viewer_thumbs import makethumbs, ViewOne
from PIL import ImageTk


def viewer(imgdir, kind=Toplevel, cols=None):
    win = kind()
    win.title('Viewer:' + imgdir)
    thumbs = makethumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs))))

    rownum = 0
    savephoto = []
    while thumbs:
        thumbrow, thumbs = thumbs[:cols], thumbs[cols:]
        colnum = 0
        for (imgfile, imgobj) in thumbrow:
            photo = ImageTk.PhotoImage(imgobj)
            link = Button(win, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler)
            link.grid(row=rownum, column=colnum)
            savephoto.append(photo)
            colnum += 1
        rownum += 1
    Button(win, text='Quit All', command=win.quit).grid(columnspan=cols, stick=EW)
    return win,savephoto

if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or '..\\images'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()