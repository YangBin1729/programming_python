#!python3
# canvasDraw.py - 使用画布事件


from tkinter import *
trace = False


class CanvasEventsDemo:
    def __init__(self, parent=None):
        canvas = Canvas(width=300, height=300, bg='beige')
        canvas.pack()
        canvas.bind('<ButtonPress-1>', self.onStart)
        canvas.bind('<B1-Motion>', self.onGrow)
        canvas.bind('<Double-1>', self.onClear)
        canvas.bind('<ButtonPress-3>', self.onMove)
        self.canvas = canvas
        self.drawn = None
        self.kinds = [canvas.create_oval, canvas.create_rectangle]

    def onStart(self, event):       # 单击鼠标
        self.shape = self.kinds[0]          # 交替画椭圆和方形的命令
        self.kinds = self.kinds[1:] + self.kinds[:1]
        self.start = event      # 保存单击鼠标事件
        self.drawn = None       # 单击鼠标，清空 drawn 参数

    def onGrow(self, event):    # 拖动鼠标
        canvas = event.widget
        if self.drawn:
            canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y)     # 单击鼠标时的坐标，和按住鼠标拖动时的坐标
        if trace:
            print(objectId)
        self.drawn = objectId

    def onClear(self, event):       # 清空画布，使用内置标签 all，关联起屏幕上所有对象
        event.widget.delete('all')

    def onMove(self, event):
        if self.drawn:
            if trace:
                print(self.drawn)
            canvas = event.widget
            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
            canvas.move(self.drawn, diffX, diffY)
            self.start = event


if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()