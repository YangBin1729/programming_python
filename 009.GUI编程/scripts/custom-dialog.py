#!python3
# custom-dialog.py - 自定义对话框


import sys
from tkinter import *

makemodal = (len(sys.argv) > 1)


def dialog():
    win = Toplevel()
    Label(win, text='Hard drive reformatted!').pack()
    Button(win, text='OK', command=win.destroy).pack()
    if makemodal:               # 脚本在有命令行参数的情况下运行，为模态对话框
        win.focus_set()         # 获得输入焦点
        win.grab_set()          # 打开时禁用其它窗口
        win.wait_window()       # 在win销毁之前，持续等待
    print('dialog exit')


root = Tk()
Button(root, text='popup', command=dialog).pack()
root.mainloop()