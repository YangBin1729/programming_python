#!python
# toplevel1.py - 多个独立的根窗口

import tkinter
from tkinter import Tk, Button
tkinter.NoDefaultRoot()

win1 = Tk()
win2 = Tk()

Button(win1, text='spam', command=win1.destroy).pack()
Button(win2, text='SPAM', command=win2.destroy).pack()

win1.mainloop()