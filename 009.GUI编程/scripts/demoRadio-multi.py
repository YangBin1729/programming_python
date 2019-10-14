#!python3
# demoRadio-multi.py - 将多个单选按钮的value属性设为相同

from tkinter import *
root = Tk()
var = StringVar()
for i in range(10):
    rad = Radiobutton(root, text=str(i), variable=var, value=str(i % 3))
    # 多个单选按钮的value值相同，选中一个时选中一组

    rad.pack(side=LEFT, fill=BOTH, expand=YES)
var.set(' ')
root.mainloop()