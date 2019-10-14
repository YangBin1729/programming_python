#!python3
# windows.py - 封装顶层窗口接口

import os
import glob
from tkinter import Tk, Toplevel, Frame, YES, BOTH, RIDGE
from tkinter.messagebox import showinfo, askyesno


class _window():
    foundicon = None        # 类属性，而不是实例属性
    iconpatt = '*.ico'
    icomine = 'py.ico'

    def configBorders(self, app, kind, iconfile):
        if not iconfile:
            iconfile = self.findIcon()
        title = app
        if kind:
            title += '-' + kind
        self.title(title)
        self.iconname(app)
        if iconfile:
            try:
                self.iconbitmap(iconfile)
            except:
                pass
        self.protocol('WM_DELETE_WINDOW', self.quit)

    def findIcon(self):
        if _window.foundicon:
            return _window.foundicon
        iconfile = None
        iconshere = glob.glob(self.iconpatt)
        if iconshere:
            iconfile = iconshere[0]
        else:
            mymod = __import__(__name__)
            path = __name__.split('.')
            for mod in path[1:]:
                mymod = getattr(mymod, mod)
            mydir = os.path.dirname(mymod.__file__)
            myicon = os.path.join(mydir, self.icomine)
            if os.path.exists(myicon):
                iconfile = myicon
        _window.foundicon = iconfile
        return iconfile


class MainWindow(Tk, _window):
    def __init__(self, app, kind='', iconfile=None):
        Tk.__init__(self)
        self._app = app
        self.configBorders(app, kind, iconfile)

    def quit(self):
        if self.okayToQuit():
            if askyesno(self._app, 'Verify Quit Program?'):
                self.destroy()
        else:
            showinfo(self._app, 'Quit Not Allowed')

    def destroy(self):
        Tk.quit(self)

    def okayToQuit(self):
        return True


class PopupWindow(Toplevel, _window):
    def __init__(self, app, kind='', iconfile=None):
        Toplevel.__init__(self)
        self._app = app
        self.configBorders(app, kind, iconfile)

    def quit(self):
        if askyesno(self._app, 'Verify Quit Window?'):
            self.destroy()

    def destroy(self):
        Toplevel.destroy(self)


class QuitPopuoWindow(PopupWindow):
    def quit(self):
        self.destory()


class ComponentWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.config(relief=RIDGE, border=2)

    def quit(self):
        showinfo('Quit', 'Not Supported in attachment mode')





