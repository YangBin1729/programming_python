::::::::::::::::::::textpak=>entry1.py
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
::::::::::::::::::::textpak=>entry2-modal.py
#!python3
# entry2-modal.py - 设置表单对话框为模态；

from tkinter import *
from entry2 import makeform, fetch, fields


def show(entries, popup):
    fetch(entries)      # 必须先获取数据，再销毁窗口
    popup.destroy()


def ask():
    popup = Toplevel()      # 基于弹出窗口创建表单
    ents = makeform(popup, fields)
    Button(popup, text='Ok', command=lambda: show(ents, popup)).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()     # 模态窗口，会阻止其它界面直至该窗口关闭


root = Tk()

Button(root, text='Dialog', command=ask).pack()
root.mainloop()
::::::::::::::::::::textpak=>entry2.py
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
::::::::::::::::::::textpak=>entry3-modal.py
#!python3
# entry3-modal.py - 使用变量对象链接至模态对话框的输入值

from tkinter import *
from entry3 import makeform, fetch, fields


def show(variables, popup):
    popup.destroy()     # 弹出窗口先销毁
    fetch(variables)    # 变量在窗口销毁后仍存在


def ask():
    popup = Toplevel()
    vars = makeform(popup, fields)
    Button(popup, text='OK', command=lambda: show(vars, popup)).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()


root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()
::::::::::::::::::::textpak=>entry3.py
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
