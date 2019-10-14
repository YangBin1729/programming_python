#!python3
# viewer-thumbs-nosave.py - 不保存缩略图，节省内存，但每次重新运行脚本都需要重新创建缩略图，大图片集启动速度变慢



import os
import sys
from PIL import Image
from tkinter import Tk
import viewer_thumbs


def makeThumbs(imgdir, size=(100, 100), subdir='thumbs'):
    thumbs = []
    for imgfile in os.listdir(imgdir):
        imgpath = os.path.join(imgdir, imgfile)
        try:
            imgobj = Image.open(imgpath)
            imgobj.thumbnail(size)
            thumbs.append((imgfile, imgobj))
        except:
            print('Skipping:', imgpath)
    return thumbs


if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or '..\images'
    viewer_thumbs.makethumbs = makeThumbs
    main, save = viewer_thumbs.viewer(imgdir, kind=Tk)
    main.mainloop()