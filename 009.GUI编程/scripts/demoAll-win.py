#!python3
# demoAll-win.py - 多个独立的顶层窗口

from tkinter import *
demoMudules = ['dialogTable', 'demoCheck', 'demoRadio', 'demoScale']


def makePopups(modnames):
    demoObjects = []
    for modname in modnames:
        module = __import__(modname)
        window = Toplevel()
        demo = module.Demo(window)
        window.title(module.__name__)
        demoObjects.append(demo)
    return demoObjects


def allstates(demoObjects):
    for obj in demoObjects:
        if hasattr(obj, 'report'):
            print(obj.__module__, end=' ')
            obj.report()


root = Tk()
root.title('Popups')
demos = makePopups(demoMudules)
Label(root, text='Multipile Toplevel window demo', bg='white').pack()
Button(root, text='States', command=lambda: allstates(demos)).pack(fill=X)
root.mainloop()