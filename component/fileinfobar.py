'''Widget displays the name of the project on top when it is created. And controls the
   focusing and deleting the project.
'''

import tkinter as tk


class FileInfoBar(tk.Text):
    def __init__(self, app, parent: tk.Widget, **kw):
        super().__init__(parent, **kw)
