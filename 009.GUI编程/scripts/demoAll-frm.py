#!python3
# demoAll-frm.py - 一个单容器中显示多个组件


from tkinter import *
from dialogTable import Quitter

demoMudules = ['dialogTable', 'demoCheck', 'demoRadio', 'demoScale']
parts = []


def  addComponents(root):
    for demo in demoMudules:
        module = __import__(demo)
        part = module.Demo(root)
        part.config(bd=2, relief=GROOVE)
        part.pack(side=LEFT, fill=BOTH, expand=YES)
        parts.append(part)


def dumpState():
    for part in parts:
        print(part.__module__+':', end=' ')
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')


root = Tk()
root.title('Frames')
Label(root, text='Multipile Frame demo', bg='white').pack()
Button(root, text='State', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()