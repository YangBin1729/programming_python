#!python3
# grid2-same.py -

from tkinter import *
from grid2 import gridbox, packbox

root = Tk()

Label(root, text='Grid:').pack()
frm = Frame(root, bd=5, relief=RAISED)
gridbox(frm)
frm.pack(padx=5, pady=5)

Label(root, text='Pack:').pack()
frm = Frame(root, bd=5, relief=RAISED)
packbox(frm)
frm.pack(padx=5, pady=5)

Button(root, text='Quit', command=root.quit).pack()
mainloop()