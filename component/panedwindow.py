import tkinter as tk
from .widgetbase import Base


class PanedWindow(tk.PanedWindow, Base):
    def __init__(self, parent: tk.Widget, **kw):
        super().__init__(parent, **kw)
