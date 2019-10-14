#!python3
# menu_frm.py - 基于框架的菜单

from tkinter import *
from tkinter.messagebox import *


def notdone():
    showerror('Not implemented', 'Not yet available')


def makemenu(parent):
    menubar = Frame(parent)
    menubar.pack(side=TOP, fill=X)

    fbutton = Menubutton(menubar, text='File', underline=0)
    fbutton.pack(side=LEFT)

    file = Menu(fbutton)
    file.add_command(label='New...', command=notdone, underline=0)
    file.add_command(label='Open...', command=notdone, underline=0)
    file.add_command(label='Quit...', command=notdone, underline=0)
    fbutton.config(menu=file)

    ebutton = Menubutton(menubar, text='Edit', underline=0)
    ebutton.pack(side=LEFT)

    edit = Menu(ebutton, tearoff=False)
    edit.add_command(label='Cut', command=notdone, underline=0)
    edit.add_command(label='Paste', command=notdone, underline=0)
    edit.add_separator()
    ebutton.config(menu=edit)

    submenu = Menu(edit, tearoff=True)
    submenu.add_command(label='Spam', command=notdone, underline=0)
    submenu.add_command(label='Eggs', command=parent.quit, underline=0)
    edit.add_cascade(label='stuff', menu=submenu, underline=0)
    return menubar


if __name__ == '__main__':
    root = Tk()
    root.title('menu-frm')
    makemenu(root)
    msg = Label(root, text='Frame Menu basic')
    msg.pack(fill=BOTH, expand=YES)
    msg.config(bd=2, relief=SUNKEN, width=40, height=7, bg='beige')
    root.mainloop()
