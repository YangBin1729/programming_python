#!python3
# demoCheck.py -

from tkinter import *
from dialogTable import demos, Quitter


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        self.tools()
        Label(self, text='Check demos').pack()
        self.vars = []
        for key in demos:
            var = IntVar()  # 初始时为空，即按钮未被选中时该变量为0，选中后变为1
            var.set(5)      # 将初始值设为5，即按钮未被选中时变量为5，选中后变为1
            Checkbutton(self, text=key, variable=var,
                        command=demos[key]).pack(side=LEFT)
            self.vars.append(var)

    def report(self):
        for var in self.vars:
            print(var.get(), end=' ')
        print()

    def tools(self):
        frm = Frame(self)
        frm.pack(side=RIGHT)
        Button(frm, text='State', command=self.report).pack(fill=X)
        Quitter(frm).pack(fill=X)


if __name__ == '__main__':
    Demo().mainloop()