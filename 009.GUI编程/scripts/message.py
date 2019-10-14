#!python3
# message.py - message组件

from tkinter import *
msg = Message(text='Oh by the way,which one is pink')
msg.config(bg='pink', font=('times', 16, 'italic'))
msg.pack(fill=X, expand=YES)

mainloop()