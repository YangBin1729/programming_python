#!python3
# viewer-tk.py -

import os
import sys
from tkinter import *

imgdir = '..\\images\\'
imgfile = 'london-2010.gif'
if len(sys.argv) > 1:   # 命令行参数给定图片路径
    imgfile = sys.argv[1]

imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)
Label(win, image=imgobj).pack()
print(imgobj.width(), imgobj.height())
win.mainloop()
