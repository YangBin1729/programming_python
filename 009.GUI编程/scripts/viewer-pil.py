#!python3
# viewer-pil.py - 显示其它格式的文件

import os
import sys
from tkinter import *
from PIL import ImageTk

imgdir = '..\images'
imgfile = 'florida-2009-1.jpg'

if len(sys.argv) > 1:   # 命令行参数给定图片路径
    imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = ImageTk.PhotoImage(file=imgpath)
Label(win, image=imgobj).pack()
print(imgobj.width(), imgobj.height())
win.mainloop()