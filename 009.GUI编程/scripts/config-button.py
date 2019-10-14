#!python3
# config-button.py - 配置按钮的外观

from tkinter import *

root = Tk()
widget = Button(root, text='spam', padx=10, pady=10)
widget.config(cursor='watch')
widget.config(bd=8, relief=GROOVE)
widget.config(bg='dark green', fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))
widget.pack(padx=20, pady=20)
mainloop()