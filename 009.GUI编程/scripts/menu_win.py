#!python3
# menu_win.py - 顶层窗口菜单


from tkinter import *
from tkinter.messagebox import *


def notdone():
    showerror('Not implemented', 'not yet availiable')


def makemenu(win):
    top = Menu(win)     # 创建顶层 Menu 作为窗口的子组件，菜单栏
    win.config(menu=top)    # 将窗口的menu属性设置为新创建的 Menu 对象
    file = Menu(top)    # 创建新的 Menu 作为顶层 Menu 的子组件
    file.add_command(label='New...', command=notdone, underline=0)      # underline 为菜单选项添加快捷方式
    file.add_command(label='Open...', command=notdone, underline=0)
    file.add_command(label='Quit', command=win.quit, underline=0)
    top.add_cascade(label='File', menu=file, underline=0)   # 给顶层 Menu 添加下拉显示对象

    edit = Menu(top, tearoff=False)
    edit.add_command(label='Cut', command=notdone, underline=0)
    edit.add_command(label='paste', command=notdone, underline=0)
    edit.add_separator()    # 在 Edit 下拉菜单中添加分割线
    top.add_cascade(label='Edit', menu=edit, underline=0)

    submenu = Menu(edit, tearoff=True)
    submenu.add_command(label='Spam', command=win.quit, underline=0)
    submenu.add_command(label='Eggs',command=notdone, underline=0)
    edit.add_cascade(label='stuff', menu=submenu, underline=0)


if __name__ == '__main__':
    root = Tk()
    root.title('menu_win')
    makemenu(root)
    msg = Label(root, text='window menu basics')
    msg.pack(expand=YES, fill=BOTH)
    msg.config(relief=SUNKEN, width=40, height=7, bg='beige')
    root.mainloop()
