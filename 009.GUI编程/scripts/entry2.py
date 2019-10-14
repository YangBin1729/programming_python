#!python3
# entry2.py - 设计输入表单


from tkinter import *
from dialogTable import Quitter
fields = 'Name', 'Job', 'Pay'


def fetch(entries):
    for entry in entries:
        print('Input=>"%s"' % entry.get())


def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)   # 基于框架的表单设计
        lab = Label(row, width=5, text=field)
        ent = Entry(row)
        row.pack(side=TOP, fill=X)      # 每组 Label 和 Entry 对象添加在 Frame 上
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append(ent)
    return entries


if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event: fetch(ents)))
    Button(root, text='Fetch', command=(lambda: fetch(ents))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.mainloop()