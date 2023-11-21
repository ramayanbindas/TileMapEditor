import tkinter as tk
from PIL import Image, ImageTk
from .project_info import DEFAULT_CANVAS_TYPE


class Canvas(tk.Canvas):
    def __init__(self, app, widget: tk.Widget, project_info: object, **kw):
        super().__init__(widget, **kw)
        self.app = app
        self.project_info = project_info

        # Adjusting the Canvas
        if self.project_info.project_type.get() == DEFAULT_CANVAS_TYPE[0]:
            self.config(scrollregion=(-999999, -999999, 999999, 999999))
        elif self.project_info.project_type.get() == DEFAULT_CANVAS_TYPE[1]:
            h_w, h_h = [round(self.project_info.canvas_width.get() / 2),
                        round(self.project_info.canvas_height.get() / 2)]
            self.config(scrollregion=(-h_w, -h_h, h_w, h_h))

        # creating widget and adding event
        self.bind_event()
        self.add()

        # variables
        self.tagid = 0
        self.grid_size = [16, 16]
        self.show_grid = tk.IntVar(self.master, 0)
        self.grid_pos_x = tk.IntVar(self.master, 0)
        self.grid_pos_y = tk.IntVar(self.master, 0)
        self.grid_pos = tk.StringVar(self.master, '0x0')
        self.canvas_size = tk.StringVar(
            self.master,
            f"{self.project_info.canvas_width.get()}x{self.project_info.canvas_height.get()}")

        # creating widget
        self.create_grid_rect()
        self.pack_widget()

    def add(self):
        ''':method: add widget into the canvas'''
        # adding a scrollbar
        self.v_scrollbar = tk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.scroll_y)
        self.config(yscrollcommand=self.v_scrollbar.set)
        self.h_scrollbar = tk.Scrollbar(self.master, orient=tk.HORIZONTAL, command=self.scroll_x)
        self.config(xscrollcommand=self.h_scrollbar.set)

        # project title button
        self.frame = tk.Frame(self.app.fileinfobar)
        self.frame.pack(side=tk.LEFT)
        tk.Button(self.frame, text=self.project_info.project_name.get()).pack(side=tk.LEFT)
        tk.Button(self.frame, text="delete", command=self.destory_widget).pack(side=tk.LEFT)

    def bind_event(self):
        ''':method: adds event releated to the canvas'''
        # self.app.root.bind("<Enter>", lambda *args: self.zoom_in())
        self.bind("<Motion>", self.change_grid_rect_pos)

    def unbind_event(self):
        self.unbind("<Motion>", self.change_grid_rect_pos)

    def pack_widget(self):
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.pack(fill=tk.BOTH, expand=True)

    def unpack_widget(self):
        self.v_scrollbar.pack_forget()
        self.h_scrollbar.pack_forget()
        self.pack_forget()

    def destory_widget(self):
        self.frame.destroy()
        self.destroy()
        self.v_scrollbar.destroy()
        self.h_scrollbar.destroy()

    def create_grid_rect(self):
        ''''''
        self.tagid += 1
        self.create_rectangle((0, 0, self.grid_size[0], self.grid_size[1]), fill="red")
        self.addtag_withtag("grid_rect", self.find_all()[-1])

    def change_grid_rect_pos(self, event):
        self.grid_pos_x.set(self.canvasx(self.winfo_pointerx() - self.winfo_rootx(),
                                         gridspacing=self.grid_size[0]))
        self.grid_pos_y.set(self.canvasy(self.winfo_pointery() - self.winfo_rooty(),
                                         gridspacing=self.grid_size[1]))

        self.grid_pos.set(f"{self.grid_pos_x.get()}x{self.grid_pos_y.get()}")
        self.moveto("grid_rect", self.grid_pos_x.get(), self.grid_pos_y.get())

    def scroll_y(self, *args):
        ''':method:'''
        self.yview(*args)

    def scroll_x(self, *args):
        ''''''
        self.xview(*args)

    def view_grid(self):
        if self.show_grid.get():
            self.draw_grid()
        else:
            self.clear_grid()

    def draw_grid(self):
        ''':method: used to draw grid over the canvas'''
        h_w, h_h = [round(self.project_info.canvas_width.get() / 2),
                    round(self.project_info.canvas_height.get() / 2)]

        c_w, c_h = [self.project_info.canvas_width.get(),
                    self.project_info.canvas_height.get()]
        x_range = round(c_w / self.grid_size[0])
        y_range = round(c_h / self.grid_size[1])
        tag = ["grid_x", "grid_y"]

        # create verticle line
        for x in range(1, x_range):
            p1 = ((x * self.grid_size[0]) - h_w, -h_h)
            p2 = ((x * self.grid_size[0]) - h_w, h_h)
            self.create_line(p1, p2)
            self.tagid += 1
            self.addtag_withtag(tag[0], self.tagid)

        # create horizontal line
        for y in range(1, y_range):
            p1 = (-h_w, (y * self.grid_size[1]) - h_h)
            p2 = (h_w, (y * self.grid_size[1]) - h_h)
            self.create_line(p1, p2)
            self.tagid += 1
            self.addtag_withtag(tag[1], self.tagid)

    def clear_grid(self):
        self.delete("grid_x")
        self.delete("grid_y")

    def zoom_in(self):
        ''':method: used to zoom all the element inside the canvas'''
        zoom_in_value = 1.5
        self.grid_size = [zoom_in_value * i for i in self.grid_size]
        # zoom the rectangle
        self.scale("grid_rect", 0, 0, zoom_in_value, zoom_in_value)
        if self.show_grid.get():
            self.clear_grid()
            self.draw_grid()

    def zoom_out(self):
        ''':method: used to zoom out all the element inside the canvas'''
        zoom_out_value = 1 / 1.5
        self.grid_size = [i * zoom_out_value for i in self.grid_size]
        # zoom the rectangle
        self.scale("grid_rect", 0, 0, zoom_out_value, zoom_out_value)
        if self.show_grid.get():
            self.clear_grid()
            self.draw_grid()
