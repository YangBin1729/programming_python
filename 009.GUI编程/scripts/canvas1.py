#!python3
# canvas1.py -

from tkinter import *

root = Tk()
canvas = Canvas(root, width=525, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)

canvas.create_line(100, 100, 200, 200)
canvas.create_line(100, 50, 200, 250)
for i in range(1, 20, 2):
    canvas.create_line(0, i, 50, i)

canvas.create_oval(10, 10, 200, 200, width=5, fill='blue')

photo = PhotoImage(file='..\images\ora-lp4e.gif')
canvas.create_image(325, 25, image=photo, anchor=NW)

widget = Label(canvas, text='Spam', fg='black', bg='white')
canvas.create_window(100, 100, window=widget)

mainloop()