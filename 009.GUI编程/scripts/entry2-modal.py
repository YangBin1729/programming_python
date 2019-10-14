#!python3
# entry2-modal.py - 设置表单对话框为模态；

from tkinter import *
from entry2 import makeform, fetch, fields


def show(entries, popup):
    fetch(entries)      # 必须先获取数据，再销毁窗口
    popup.destroy()


def ask():
    popup = Toplevel()      # 基于弹出窗口创建表单
    ents = makeform(popup, fields)
    Button(popup, text='Ok', command=lambda: show(ents, popup)).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()     # 模态窗口，会阻止其它界面直至该窗口关闭


root = Tk()

Button(root, text='Dialog', command=ask).pack()
root.mainloop()
