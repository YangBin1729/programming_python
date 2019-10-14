#!python3
# mbutton.py - Menubutton 不创建于菜单栏上

from tkinter import *
root = Tk()
mbutton = Menubutton(root, text='Food')
picks = Menu(mbutton)
mbutton.config(menu=picks)
picks.add_command(label='Spam', command=root.quit)
picks.add_command(label='eggs', command=root.quit)
picks.add_command(label='bacons', command=root.quit)

mbutton.pack()
mbutton.config(bg='white', bd=4, relief=RAISED)
root.mainloop()