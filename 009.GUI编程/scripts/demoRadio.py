#!python3
# demoRadio.py -


from tkinter import *
from dialogTable import demos, Quitter


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text='Radio demos').pack(side=TOP)
        self.var = StringVar()
        for key in demos:
            Radiobutton(self, text=key, command=self.onPress,
                        variable=self.var, value=key).pack(anchor=NW)
            # 每个单选按钮设定了不同的value值，但关联了同一个变量 self.var
            # 哪个按钮被选中，共享变量self.var的值即变为该按钮的value

        self.var.set(key)
        Button(self, text='State', command=self.report).pack(fill=X)
        Quitter(self).pack(fill=X)

    def onPress(self):
        pick = self.var.get()
        print('you pressed ', pick)
        print('result:', demos[pick]())

    def report(self):
        print(self.var.get())


if __name__ == '__main__':
    Demo().mainloop()