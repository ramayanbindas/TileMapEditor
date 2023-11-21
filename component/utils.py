''''''
from tkinter import filedialog
from .canvas import Canvas
from .project_info import ProjectInfo


class FileDialog:
    def __init__(self, master):
        # self.master = master
        self.filename = None

    def open(self):
        self.filename = filedialog.askopenfilename()


def create_new_project(app, parent, **kw):
    project_info = ProjectInfo(app)
    return Canvas(app, parent, project_info, **kw)
