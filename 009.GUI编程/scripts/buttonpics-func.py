#!python3
# buttonpics-func.py -


from tkinter import *
from glob import glob
import demoCheck
import random

gifdir = '../images/'


def draw():
    name, photo = random.choice(images)
    lbl.config(text=name)
    pix.config(image=photo)


root = Tk()
lbl = Label(root, text='None', bg='black', fg='red')
pix = Button(root, text='Press me', command=draw, bg='white')
lbl.pack(fill=BOTH)
pix.pack(pady=10)
demoCheck.Demo(root, relief=SUNKEN, bd=2).pack(fill=BOTH)

files = glob(gifdir+'*.gif')
images = [(x, PhotoImage(file=x)) for x in files]
print(files)
root.mainloop()
