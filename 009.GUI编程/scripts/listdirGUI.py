#!python3
# listdirGUI.py - GUI程序，遍历目录，显示其中所有文件夹及文件

import os
from time import sleep
from tkinter import *


class DirList():
    def __init__(self, initdir=None):
        self.initdir = initdir

        # 第一个Label控件，应用的主标题及版本号
        self.top = Tk()
        self.label = Label(self.top, text='Directory Lister v1.1')
        self.label.pack()

        # 声明了Tk的一个变量cwd，用于保存当前目录名
        self.cwd = StringVar(self.top)

        # Label控件用于显示当前目录名
        self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
        self.dirl.pack()

        # 定义Listbox控件dirs，包含有列出的文件列表；Scrollbar用来上下滚动；
        # Listbox的列表项与回调函数setDirAndGo绑定
        # 两个控件都包含在Frame控件中
        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)

        self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=LEFT, fill=BOTH)

        self.dirfm.pack()

        # 创建文本框，输入想要遍历的目录名；该文本框添加了一个 回车键 的绑定
        self.dirn = Entry(self.top, width=50, textvariable=self.cwd)
        self.dirn.bind('<Return>', self.doLS)
        self.dirn.pack()

        # 定义了按钮的框架，用来放置3个按钮：clear、List Directory、Quit，每个按钮有其自己的配置和回调函数
        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='Clear', command=self.clrDir,
                          activeforeground='white',
                          activebackground='blue')
        self.ls = Button(self.bfm, text='List Directory', command=self.doLS,
                         activeforeground='white',
                         activebackground='green')
        self.quit = Button(self.bfm, text='Quit', command=self.top.quit,
                          activeforeground='white',
                          activebackground='red')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()

        # 初始化程序，并以当前工作目录作为起点
        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()

    # 清空Tk变量cwd
    def clrDir(self, ev=None):
        self.cwd.set('')

    # 设置要遍历的目录，并调用doLS函数
    def setDirAndGo(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    # 进行安全检查，
    def doLS(self, ev=None):
        error = ''
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir
        if not os.path.exists(tdir):
            error = tdir + ':no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ':no such directory'
        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='ListSkyBlue')
            self.top.update()
            return

        self.cwd.set('FETCHING DIRECTORY CONTENTS...')
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)

        self.dirl.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        for eachfile in dirlist:
            self.dirs.insert(END, eachfile)

        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')

def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()
