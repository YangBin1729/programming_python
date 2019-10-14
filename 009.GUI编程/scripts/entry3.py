#!python3
# entry3.py - 使用StringVar变量对象来获取输入框的值

from tkinter import *
from dialogTable import Quitter

fields = 'Name', 'Job', 'Pay'


def fetch(variables):
    for variable in variables:
        print('Input =>"%s"' % variable.get())  # 从变量对象中获取Entry组件的输入值


def makeform(root, fields):
    form = Frame(root)
    left = Frame(form)
    rite = Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    rite.pack(side=RIGHT, expand=YES, fill=X)
    variables = []
    for field in fields:
        lab = Label(left, width=5, text=field)
        ent = Entry(rite)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)
        var = StringVar()
        ent.config(textvariable=var)  # 利用变量对象来获取输入框的文本
        var.set('Enter here')
        variables.append(var)
    return variables


if __name__ == '__main__':
    root = Tk()
    vars = makeform(root, fields)
    Button(root, text='Fetch', command=lambda: fetch(vars)).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', lambda event: fetch(vars))
    root.mainloop()