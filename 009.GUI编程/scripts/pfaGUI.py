#!python3
# pfaGUI.py - 根据标志类型创建拥有合适前景色和背景色的图标。使用偏函数‘模板化’通用的GUI参数


from functools import partial as pto
from tkinter import Tk, Button, X
from tkinter.messagebox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNs = {'do not enter': CRIT,
         'railroad crossing': WARN,
         '55\nspeed limit': REGU,
         'wrong way': CRIT,
         'merging traffic': WARN,
         'one way': REGU}

critCB = lambda: showerror('Error', 'Error Button Pressed')
warnCB = lambda: showwarning('Warning', 'Waring Button Pressed')
infoCB = lambda: showinfo('Info', 'Info Button Pressed')

top = Tk()
top.title('Road Signs')
Button(top, text='QUIT!', command=top.quit, bg='red', fg='white').pack()

MyButton = pto(Button, top)
CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='goldenrod1')
ReguButton = pto(MyButton, command=infoCB, bg='white')

for eachsign in SIGNs:
    signtype = SIGNs[eachsign]
    cmd = '%sButton(text=%r%s).pack(fill=X,expand=True)'% (signtype.title(), eachsign,
                                                           '.upper()' if signtype==CRIT else '.title()')
    eval(cmd)

top.mainloop()
