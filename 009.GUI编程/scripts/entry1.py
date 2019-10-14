#!python3
# entry1.py -

from tkinter import *
from dialogTable import Quitter


def fetch():        # 获取文本输入框类文本
    print('Input =>"%s"' % ent.get())


root = Tk()
ent = Entry(root, show='*')
ent.insert(0, 'Type words here')
ent.pack(side=TOP, fill=X)

ent.focus()     # 设置得出输入字段的输入焦点，可以使用户在输入前不必单击输入框
ent.bind('<Return>', (lambda event: fetch()))
btn = Button(root, text='Fetch', command=fetch)
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()