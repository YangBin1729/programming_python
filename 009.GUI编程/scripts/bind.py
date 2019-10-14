#!python3
# bind.py - 绑定事件

from tkinter import *


def showPoseEvent(event):
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))


def showAllEvent(event):
    print(event)
    for attr in dir(event):         # 所有的事件属性，获取事件的相关信息
        if not attr.startswith('__'):
            print(attr, '=>', getattr(event, attr))


def onKeyPress(event):
    print('Got key press:', event.char)


def onArrowKey(event):
    print('Got up arrow key press')


def onReturnKey(event):
    print('Got return key press')


def onLeftClick(event):
    print('Got left mouse button click:', end=' ')
    showPoseEvent(event)


def onRightClick(event):
    print('Got right mouse button clcik:', end=' ')
    showPoseEvent(event)


def onMiddleClick(event):
    print('Got middle mouse button click:', end=' ')
    showPoseEvent(event)
    showAllEvent(event)


def onLeftDrag(event):
    print('Got left mouse button drag:', end=' ')
    showPoseEvent(event)


def onDoubleLeftClick(event):
    print('Got double left mouse click:', end=' ')
    showPoseEvent(event)
    showAllEvent(event)


tkroot = Tk()
labelfont = ('courier', 20, 'bold')
widget = Label(tkroot, text='Hello bind world')
widget.config(bg='red', font=labelfont)
widget.config(height=5, width=20)
widget.pack(expand=YES, fill=BOTH)

widget.bind('<Button-1>', onLeftClick)          # 鼠标左键单击
widget.bind('<Button-3>', onRightClick)         # 鼠标右键单击
widget.bind('<Button-2>', onMiddleClick)        # 鼠标中键单击

widget.bind('<Double-1>', onDoubleLeftClick)    # 鼠标左键双击
widget.bind('<B1-Motion>', onLeftDrag)          # 单击鼠标左键并拖动

widget.bind('<KeyPress>', onKeyPress)           # 按下左右键盘键
widget.bind('<Up>', onArrowKey)                 # 按下箭头键
widget.bind('<Return>', onReturnKey)            # 按下返回\回车键
widget.focus()
tkroot.title('Click Me')
tkroot.mainloop()
