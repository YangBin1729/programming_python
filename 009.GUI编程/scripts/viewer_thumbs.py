#!python3
# viewer_thumbs.py - 创建缩略图在GUI中显示，根据需要，打开原始大小的图片

import os
import sys
import math
from tkinter import *
from PIL import Image, ImageTk


def makethumbs(imgdir, size=(100, 100), subdir='thumbs'):
    thumbdir = os.path.join(imgdir, subdir)
    if not os.path.exists(thumbdir):
        os.mkdir(thumbdir)

    thumbs = []
    for imgfile in os.listdir(imgdir):
        thumbpath = os.path.join(thumbdir, imgfile)
        if os.path.exists(thumbpath):
            thumbobj = Image.open(thumbpath)     # 使用已经创建好的
            thumbs.append((imgfile, thumbobj))
        else:
            print('making', thumbpath)
            imgpath = os.path.join(imgdir, imgfile)
            try:
                imgobj = Image.open(imgpath)
                imgobj.thumbnail(size, Image.ANTIALIAS)     # 缩小尺寸过滤器
                imgobj.save(thumbpath)          # 所有缩略图被保存，下一次运行脚本时快速载入
                thumbs.append((imgfile, imgobj))
            except:
                print('skipping:', imgpath)
    return thumbs


class ViewOne(Toplevel):    # 显示原始图片
    def __init__(self, imgdir, imgfile):
        Toplevel.__init__(self)
        self.title(imgfile)
        imgpath = os.path.join(imgdir, imgfile)

        imgobj = ImageTk.PhotoImage(file=imgpath)
        Label(self, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height())
        self.savephoto = imgobj     # 保留对图像的引用


def viewer(imgdir, kind=Toplevel, cols=None):
    win = kind()
    win.title('Viewer:'+imgdir)
    quit = Button(win, text='Quit', command=win.quit, bg='beige')
    quit.pack(fill=X, side=BOTTOM)
    thumbs = makethumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs))))   # 固定每行显示的缩略图的个数

    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
        row = Frame(win)
        row.pack(fill=BOTH)
        for (imgfile, imgobj) in thumbsrow:
            photo = ImageTk.PhotoImage(imgobj)
            link = Button(row, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler)
            link.pack(side=LEFT, expand=YES)
            savephotos.append(photo)
    return win, savephotos


if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or '..\\images'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()