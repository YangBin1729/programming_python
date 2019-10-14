#!python3
# simpleedit.py - 添加文本编辑操作（文件保存、文本剪切和黏贴、字符串查找）

from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.filedialog import asksaveasfilename
from dialogTable import Quitter
from scrolledtext import ScrolledText


class SimpleEditor(ScrolledText):
    def __init__(self, parent=None, file=None):
        frm = Frame(parent)
        frm.pack(fill=X)
        Button(frm, text='Save', command=self.onSave).pack(side=LEFT)
        Button(frm, text='Cut', command=self.onCut).pack(side=LEFT)
        Button(frm, text='Paste', command=self.onPaste).pack(side=LEFT)
        Button(frm, text='Find', command=self.onFind).pack(side=LEFT)
        Quitter(frm).pack(side=LEFT)
        ScrolledText.__init__(self, parent, file=file)
        self.text.config(font=('courier', 12, 'normal'))

    def onSave(self):
        filename = asksaveasfilename()
        if filename:
            alltext = self.gettext()
            open(filename, 'w').write(alltext)

    def onCut(self):
        text = self.text.get(SEL_FIRST, SEL_LAST)   # 光标选中的部分
        self.text.delete(SEL_FIRST, SEL_LAST)
        self.clipboard_clear()      # 剪贴板接口
        self.clipboard_append(text)

    def onPaste(self):
        try:
            text = self.selection_get(selection='CLIPBOARD')
            self.text.insert(INSERT, text)
        except TclError:
            pass

    def onFind(self):   # 查找第一个匹配的对象，有多个匹配的应该如何实现？？？？
        target = askstring('SimpleEditor', 'Search String?')
        if target:
            where = self.text.search(target, INSERT, END)       # 从光标开始处到结尾
            if where:
                print(where)
                pastit = where + ('+%dc' % len(target))
                self.text.tag_add(SEL, where, pastit)
                self.text.mark_set(INSERT, pastit)
                self.text.see(INSERT)
                self.text.focus()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        SimpleEditor(file=sys.argv[1]).mainloop()
    else:
        SimpleEditor().mainloop()