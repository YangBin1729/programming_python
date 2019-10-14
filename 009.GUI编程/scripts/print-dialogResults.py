#!python3
# print-dialogResults.py - 点击按钮打印对话框结果

from tkinter import *
from dialogTable import Quitter, demos


class Demo(Frame):
    """
    显示按下Button后调用对话框后的返回值
    """
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text='Basic Demos').pack()
        for key in demos:
            func = (lambda key=key: self.printit(key))      # 使用 lambda 函数传递回调数据
            Button(self, text=key, command=func).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)

    def printit(self, name):
        print(name, 'returns=>', demos[name]())


if __name__ == '__main__':
    Demo().mainloop()
