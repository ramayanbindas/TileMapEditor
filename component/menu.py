'''Menu for the software.'''
import tkinter as tk
from .about import About


class Menu(tk.Menu):
    def __init__(self, app, widget: tk.Widget, **kw):
        super().__init__(widget, **kw)
        # add the menu to the widget
        self.app = app
        self.event()
        self.add_menu()
        self.master.config(menu=self)

    def add_menu(self):
        ''':method: add menu to the software as well as define the functionality of the
            menu widgets
        '''

        # File Menu
        file_menu = tk.Menu(tearoff=False)
        file_menu.add_command(label="Open Project",
                              accelerator="Ctrl+o")
        file_menu.add_command(label="New Project",
                              accelerator="Ctrl+n")
        file_menu.add_command(label="Quit", command=self.master.destroy,
                              accelerator="Ctrl+q")
        self.add_cascade(label="File", menu=file_menu)
        # Edit Menu
        self.add_cascade(label="Edit")
        # View Menu
        view_menu = tk.Menu(tearoff=False)
        view_menu.add_checkbutton(label="Show Grid",
                                  variable=self.app.current_focused_canvas.show_grid,
                                  command=self.app.current_focused_canvas.view_grid)
        self.add_cascade(label="View", menu=view_menu)
        # Help Menu
        help_menu = tk.Menu(tearoff=False)
        help_menu.add_command(label="About", command=lambda: About(self.app, self.master))
        self.add_cascade(label="Help", menu=help_menu)

    def event(self):
        ''':method: add event to related to the menu and the other widget its handle'''
        pass
