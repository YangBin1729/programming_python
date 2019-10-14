#!python3
# viewer-dir.py - 在弹出窗口显示同一目录下的所有图像

import os
import sys
from tkinter import *
from PIL import ImageTk

imgdir = '..\images'
if len(sys.argv) > 1:
    imgdir = sys.argv[1]
imgfiles = os.listdir(imgdir)

main = Tk()
main.title('Viewer')
quit = Button(main, text='Quit All', command=main.quit, font=('courier', 25))
quit.pack()
savephotos = []

for img in imgfiles:
    imgpath = os.path.join(imgdir, img)
    win = Toplevel()
    win.title(img)
    try:
        imgobj = ImageTk.PhotoImage(file=imgpath)
        Label(win, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height())
        savephotos.append(imgobj)
    except:
        errmsg = 'skipping %s\n%s' % (img, sys.exc_info()[1])
        Label(win, text=errmsg).pack()

main.mainloop()

