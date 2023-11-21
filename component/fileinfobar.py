import tkinter as tk


class FileInfoBar(tk.Text):
    def __init__(self, app, parent: tk.Widget, **kw):
        super().__init__(parent, **kw)
