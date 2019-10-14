#!python3
# dialogTable.py - 标准对话框使用示例

from tkinter import *
from tkinter.messagebox import askokcancel, askquestion, showerror
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.simpledialog import askfloat


class Quitter(Frame):
    """
    验证退出请求的Quit按钮；封装成类，可复用、连接其它GUI实例
    """
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel('Verify exit', 'Really quit?')        # 返回True或False
        if ans:
            Frame.quit(self)


demos = {'Open': askopenfilename,
         'Color': askcolor,             # 返回表示所选颜色的数据结构或元组(None,None)
         'Query': lambda: askquestion('warning', 'You typed "rm*"\nConfirm?'),  # 返回字符串'Yes'或'No'
         'Error': lambda: showerror('Error!', 'He is dead,Jack'),
         'Input': lambda: askfloat('Entry', 'Enter credit card number')}        # 返回浮点数字对象或None


class Demo(Frame):
    """
    创建简单的按钮栏，实现 demos 中的功能
    """
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text='Basic Demos').pack()
        for (key, value) in demos.items():
            Button(self, text=key, command=value).pack(fill=BOTH, side=TOP)
        Quitter(self).pack(side=TOP, fill=BOTH)

if __name__ == '__main__':
    Demo().mainloop()


