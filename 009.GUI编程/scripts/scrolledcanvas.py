#!python3
# scrolledcanvas.py -

from tkinter import *

class ScrolledCanvas(Frame):
    def __init__(self, parent=None, color='white'):
        Frame.__init__(self, parent=None)
        self.pack(expand=YES, fill=BOTH)
        canv = Canvas(self, bg=color, relief=SUNKEN)
        canv.config(width=500, height=300)      # 查看窗口的大小
        canv.config(scrollregion=(0, 0, 500, 800))      # 可滚动尺寸的大小
        canv.config(highlightthickness=0)       # 自动边框，如果宽度设为2，此时查看窗口宽度为500-2

        sbar = Scrollbar(self)
        sbar.config(command=canv.yview)
        canv.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        canv.pack(side=LEFT, expand=YES, fill=BOTH)

        self.fillContent(canv)
        canv.bind('<Double-1>', self.onDoubleClick)
        self.canvas = canv

    def fillContent(self, canv):
        for i in range(10):
            canv.create_text(150, 50+(i*100), text='spam'+str(i), fill='red')

    def onDoubleClick(self, event):
        print(event.x, event.y)
        print(self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        # 显示区域上的坐标，转化为可滚动画布上的坐标


if __name__ == '__main__':
    ScrolledCanvas().mainloop()
