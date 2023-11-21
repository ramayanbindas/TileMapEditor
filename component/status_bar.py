''''''
import tkinter as tk


class StatusBar(tk.Frame):
    def __init__(self, app, parent: tk.Widget, **kw):
        super().__init__(parent, **kw)
        self.app = app
        self.add()

    def add(self):
        ''':method: add widget into the statusbar'''
        tk.Button(self, text="zoom_in",
                  command=self.app.current_focused_canvas.zoom_in).pack(side=tk.RIGHT)
        tk.Button(self, text="zoom_out",
                  command=self.app.current_focused_canvas.zoom_out).pack(side=tk.RIGHT)
        tk.Label(self, textvariable=self.app.current_focused_canvas.grid_pos).pack(side=tk.LEFT)
        tk.Label(self, textvariable=self.app.current_focused_canvas.canvas_size).pack(side=tk.LEFT)
