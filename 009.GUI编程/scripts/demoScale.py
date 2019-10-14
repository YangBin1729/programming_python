#!python3
# demoScale.py -

from tkinter import *
from dialogTable import demos, Quitter


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text='Scale demos').pack()
        self.var = IntVar()

        # 两个Scale对象设置同样的variable，滑动一个标尺，另一个标尺位置自动变化
        Scale(self, label='Pick demo number',
              command=self.onMove, variable=self.var,
              from_=0, to=len(demos)-1).pack()
        Scale(self, label='Pick demo number',
              command=self.onMove, variable=self.var,   # command 对应的回调函数会自动获取对象值作为参数
              from_=0, to=len(demos)-1,
              length=200, tickinterval=1,
              showvalue=YES, orient='horizontal').pack()

        Quitter(self).pack(side=LEFT)
        Button(self, text='Run demo', command=self.onRun).pack(side=LEFT)
        Button(self, text='State', command=self.report).pack(side=RIGHT)

    def onMove(self, value):
        print('in move ', value)

    def onRun(self):
        pos = self.var.get()
        print('You picked ', pos)
        demo = list(demos.values())[pos]
        print(demo())

    def report(self):
        print(self.var.get())


if __name__ == '__main__':
    print(list(demos.keys()))
    Demo().mainloop()

