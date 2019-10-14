#!python3
# imageButton.py -

from tkinter import *
gifdir = '../images/'
win = Tk()
igm = PhotoImage(file=gifdir+'ora-pp.gif')
Button(win, image=igm).pack()
win.mainloop()