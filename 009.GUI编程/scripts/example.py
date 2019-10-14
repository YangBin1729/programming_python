::::::::::::::::::::textpak=>entry1.py
#!python3
# entry1.py -

from tkinter import *
from dialogTable import Quitter


def fetch():        # ��ȡ�ı���������ı�
    print('Input =>"%s"' % ent.get())


root = Tk()
ent = Entry(root, show='*')
ent.insert(0, 'Type words here')
ent.pack(side=TOP, fill=X)

ent.focus()     # ���õó������ֶε����뽹�㣬����ʹ�û�������ǰ���ص��������
ent.bind('<Return>', (lambda event: fetch()))
btn = Button(root, text='Fetch', command=fetch)
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()
::::::::::::::::::::textpak=>entry2-modal.py
#!python3
# entry2-modal.py - ���ñ��Ի���Ϊģ̬��

from tkinter import *
from entry2 import makeform, fetch, fields


def show(entries, popup):
    fetch(entries)      # �����Ȼ�ȡ���ݣ������ٴ���
    popup.destroy()


def ask():
    popup = Toplevel()      # ���ڵ������ڴ�����
    ents = makeform(popup, fields)
    Button(popup, text='Ok', command=lambda: show(ents, popup)).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()     # ģ̬���ڣ�����ֹ��������ֱ���ô��ڹر�


root = Tk()

Button(root, text='Dialog', command=ask).pack()
root.mainloop()
::::::::::::::::::::textpak=>entry2.py
#!python3
# entry2.py - ��������


from tkinter import *
from dialogTable import Quitter
fields = 'Name', 'Job', 'Pay'


def fetch(entries):
    for entry in entries:
        print('Input=>"%s"' % entry.get())


def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)   # ���ڿ�ܵı����
        lab = Label(row, width=5, text=field)
        ent = Entry(row)
        row.pack(side=TOP, fill=X)      # ÿ�� Label �� Entry ��������� Frame ��
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
# entry3-modal.py - ʹ�ñ�������������ģ̬�Ի��������ֵ

from tkinter import *
from entry3 import makeform, fetch, fields


def show(variables, popup):
    popup.destroy()     # ��������������
    fetch(variables)    # �����ڴ������ٺ��Դ���


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
# entry3.py - ʹ��StringVar������������ȡ������ֵ

from tkinter import *
from dialogTable import Quitter

fields = 'Name', 'Job', 'Pay'


def fetch(variables):
    for variable in variables:
        print('Input =>"%s"' % variable.get())  # �ӱ��������л�ȡEntry���������ֵ


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
        ent.config(textvariable=var)  # ���ñ�����������ȡ�������ı�
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
