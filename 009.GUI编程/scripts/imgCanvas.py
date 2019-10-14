#!python3
# imgCanvas.py -

from tkinter import *
gifdir = '../images/'
win = Tk()
img = PhotoImage(file=gifdir+'ora-lp4e.gif')
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=img, anchor=NW)    # x和y坐标
win.mainloop()
