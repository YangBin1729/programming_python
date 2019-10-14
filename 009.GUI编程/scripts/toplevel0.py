#!python3
# toplevel0.py - Toplevel对象

import sys
from tkinter import Toplevel, Button, Label

win1 = Toplevel()       # 两个独立的顶层窗口，此时已默认创建了一个根窗口
win2 = Toplevel()

Button(win1, text='spam', command=sys.exit).pack()
Button(win2, text='SPAM', command=sys.exit).pack()

Label(text='Popups').pack()

win1.mainloop()