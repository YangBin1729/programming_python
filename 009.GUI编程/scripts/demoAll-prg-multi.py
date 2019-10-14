#!python3
# demoAll-prg-multi.py - 退出一个窗口不影响其它窗口


from tkinter import *
from multiprocessing import Process
demoMudules = ['dialogTable', 'demoCheck', 'demoRadio', 'demoScale']


def runDemo(modname):
    module = __import__(modname)
    module.Demo().mainloop()


if __name__ == '__main__':
    for modname in demoMudules:
        Process(target=runDemo, args=(modname,)).start()

    root = Tk()
    root.title('Process')
    Label(root, text='Multiple program demo:multiprocessing', bg='white').pack()
    root.mainloop()

