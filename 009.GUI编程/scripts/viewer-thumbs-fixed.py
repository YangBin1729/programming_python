#!python3
# viewer-thumbs-fixed.py - 固定以缩略图为背景的按钮的大小

import sys
import math
from tkinter import *
from PIL import ImageTk
from viewer_thumbs import makethumbs, ViewOne


def viewer(imgdir, kind=Toplevel, cols=None):
    win = kind()
    win.title('Viewer:' + imgdir)
    thumbs = makethumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs))))

    savephotos = []
    while thumbs:
        thumbrow, thumbs = thumbs[:cols], thumbs[cols:]
        row = Frame(win)
        row.pack(fill=BOTH)
        for (imgfile, imgobj) in thumbrow:
            size = max(imgobj.size)
            photo = ImageTk.PhotoImage(imgobj)
            link = Button(row, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler, width=size, height=size)
            link.pack(side=LEFT, expand=YES)
            savephotos.append(photo)

    Button(win, text='Quit', command=win.quit, bg='beige').pack(fill=X)
    return win, savephotos


if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or '..\\images'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()