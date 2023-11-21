''''''
import tkinter as tk

# CONSTANTS
DEFAULT_PROJECTNUM = 1
DEFAULT_PROJECTNAME = f"untitled{DEFAULT_PROJECTNUM}.json"
DEFAULT_CANVAS_TYPE = ("infinity", "fixed")
DEFUALT_GIRD_SIZE = (16, 16)
DEFAULT_CANVAS_SIZE = (1200, 800)


class ProjectInfoMessage(tk.Toplevel):
    def __init__(self, app, parent: tk.Widget, **kw):
        super().__init__(parent, **kw)
        # design
        rel_w = round(self.master.winfo_width() * 0.2)
        rel_h = round(self.master.winfo_height() * 0.24)
        x = round((self.master.winfo_width() - rel_w) / 2)
        y = round((self.master.winfo_height() - rel_h) / 2)
        self.geometry(f"{rel_w}x{rel_h}+{x}+{y}")
        self.title("Create Project")

        self.load_data()

    def load_data(self):
        ''':method: loads the data'''
        self.project_name = tk.StringVar()
        self.project_type = tk.StringVar()
        self.grid_width = tk.IntVar()
        self.grid_height = tk.IntVar()
        self.canvas_width = tk.IntVar()
        self.canvas_height = tk.IntVar()
        self.project_name.set(DEFAULT_PROJECTNAME)
        self.project_type.set(DEFAULT_CANVAS_TYPE[1])
        self.grid_width.set(DEFUALT_GIRD_SIZE[0])
        self.grid_height.set(DEFUALT_GIRD_SIZE[1])
        self.canvas_width.set(DEFAULT_CANVAS_SIZE[0])
        self.canvas_height.set(DEFAULT_CANVAS_SIZE[1])

    def add(self):
        tk.Label(self, text="Project Name:").grid(row=0, column=0, sticky=tk.NSEW)
        tk.Entry(self, textvariable=self.project_name).grid(row=0, column=1, sticky=tk.NSEW)

        tk.Label(self, text="Grid Width:").grid(row=1, column=0, sticky=tk.NSEW)
        tk.Entry(self, textvariable=self.grid_width).grid(row=1, column=1, sticky=tk.NSEW)

        tk.Label(self, text="Grid Height:").grid(row=2, column=0, sticky=tk.NSEW)
        tk.Entry(self, textvariable=self.grid_height).grid(row=2, column=1, sticky=tk.NSEW)

        tk.Label(self, text="Canvas Width:").grid(row=3, column=0, sticky=tk.NSEW)
        tk.Entry(self, textvariable=self.canvas_width).grid(row=3, column=1, sticky=tk.NSEW)

        tk.Label(self, text="Canvas Height:").grid(row=4, column=0, sticky=tk.NSEW)
        tk.Entry(self, textvariable=self.canvas_height).grid(row=4, column=1, sticky=tk.NSEW)

        tk.Button(self, text="Cancel").grid(row=5, column=0, sticky=tk.E)
        tk.Button(self, text="Create",
                  command=self.create_canvas_info).grid(row=5, column=1, sticky=tk.E)

    def create_canvas_info(self):
        if self.project_name.get():
            self.project_name.set(DEFAULT_PROJECTNAME)
        if self.grid_width.get():
            self.grid_width.set(DEFUALT_GIRD_SIZE[0])
        if self.grid_height.get():
            self.grid_height.set(DEFUALT_GIRD_SIZE[1])
        if self.canvas_width.get():
            self.canvas_width.set(DEFAULT_CANVAS_SIZE[0])
        if self.canvas_height.get():
            self.canvas_height.set(DEFAULT_CANVAS_SIZE[1])

        self.destroy()
        self.unbind_event()

    def bind_event(self):
        pass

    def unbind_event(self):
        pass

    def open(self):
        self.load_data()
        self.add()
        self.event()


class ProjectInfo:
    def __init__(self, app):
        self.project_name = tk.StringVar()
        self.project_type = tk.StringVar()
        self.grid_width = tk.IntVar()
        self.grid_height = tk.IntVar()
        self.canvas_width = tk.IntVar()
        self.canvas_height = tk.IntVar()
        self.project_name.set(DEFAULT_PROJECTNAME)
        self.project_type.set(DEFAULT_CANVAS_TYPE[1])
        self.grid_width.set(DEFUALT_GIRD_SIZE[0])
        self.grid_height.set(DEFUALT_GIRD_SIZE[1])
        self.canvas_width.set(DEFAULT_CANVAS_SIZE[0])
        self.canvas_height.set(DEFAULT_CANVAS_SIZE[1])

    def create_project_info(self):
        if self.project_name.get():
            self.project_name.set(DEFAULT_PROJECTNAME)
        if self.grid_width.get():
            self.grid_width.set(DEFUALT_GIRD_SIZE[0])
        if self.grid_height.get():
            self.grid_height.set(DEFUALT_GIRD_SIZE[1])
        if self.canvas_width.get():
            self.canvas_width.set(DEFAULT_CANVAS_SIZE[0])
        if self.canvas_height.get():
            self.canvas_height.set(DEFAULT_CANVAS_SIZE[1])


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800+0+0")
    tk.Button(text="press me", command=lambda: ProjectInfo(None, root)).pack(side=tk.TOP)
    root.mainloop()
