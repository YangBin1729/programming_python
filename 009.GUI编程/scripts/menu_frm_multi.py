#!python3
# menu_frm_multi.py - 基于框架的菜单，可以作为其它部件的组件包

from menu_frm import makemenu
from tkinter import *


root = Tk()
for i in range(3):
    frm = Frame()
    menubar = makemenu(frm)
    menubar.config(bd=2, relief=RAISED)
    frm.pack(expand=YES, fill=BOTH)
    Label(frm, text='Menu %s based on Frame' % i, bg='black', fg='yellow',
          height=5, width=25).pack(expand=YES, fill=BOTH)

Button(root, text='Bye', command=root.quit).pack()
root.mainloop()