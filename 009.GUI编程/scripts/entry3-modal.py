#!python3
# entry3-modal.py - 使用变量对象链接至模态对话框的输入值

from tkinter import *
from entry3 import makeform, fetch, fields


def show(variables, popup):
    popup.destroy()     # 弹出窗口先销毁
    fetch(variables)    # 变量在窗口销毁后仍存在


def ask():
    popup = Toplevel()
    vars = makeform(popup, fields)
    Button(popup, text='OK', command=lambda: show(vars, popup)).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()


root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()