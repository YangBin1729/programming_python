#!python3
# imgCanvas2.py -

from sys import argv
from tkinter import *

gifdir = '../images/'
filename = argv[1] if len(argv) > 1 else 'ora-lp4e.gif'   # 通过命令行输入图片地址

win = Tk()
img = PhotoImage(file=gifdir+filename)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()