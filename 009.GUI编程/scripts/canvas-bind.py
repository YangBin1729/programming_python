#!python3
# canvas-bind.py -

from tkinter import *


def onCanvasClick(event):
    print('Got canvas click', event.x, event.y, event.widget)


def onObjClick(event):
    print('Got object click', event.x, event.y, event.widget, end=' ')
    print(event.widget.find_closest(event.x, event.y))


root = Tk()
canv = Canvas(root, width=200, height=200)
obj1 = canv.create_text(80, 50, text='Click me one', font=('times', 20, 'bold'))
obj2 = canv.create_text(80, 80, text='Click me two', font=('times', 20, 'bold'))

canv.bind('<Double-1>', onCanvasClick)
canv.tag_bind(obj1, '<Double-1>', onObjClick)
canv.tag_bind(obj2, '<Double-1>', onObjClick)

canv.pack()
root.mainloop()