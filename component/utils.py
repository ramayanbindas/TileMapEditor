'''Script contain all the necessary function, and class that are needed for all the scripts'''
from tkinter import filedialog
from .canvas import Canvas
from .project_info import ProjectInfo


class FileDialog:
    '''class: handels the dialog related to the file, handling(i.e fileopendialog, ..)'''

    def __init__(self, master):
        # self.master = master
        self.filename = None

    def open(self):
        self.filename = filedialog.askopenfilename()


def create_new_project(app, parent, **kw):
    '''fuction: create a new porject with the help of information passed.
        :param app: is the instance of the main `TileMapEditor` class
        :param parent: as the name suggest the name of the parent class in which
        the canvas is being blit.
    '''
    project_info = ProjectInfo(app)
    return Canvas(app, parent, project_info, **kw)
