'''
TileMapEditor:
TileMapEditor is a versatile editor designed for 2D game development.
It provides a user-friendly interface for editing tile maps and stands out
with its unique feature allowing users to customize the data storage format
for their games. All data is saved in the widely supported JSON file format.

Features
    Customizable Data Format: Users have the freedom to design and store their
    game data in a format that suits their specific needs, thanks to the flexibility
    of the JSON file structure.

    Intuitive Tile Map Editing: The editor offers a straightforward and easy-to-use
    interface for editing tile maps, streamlining the game development process.

author: Ramayan Mardi
email: ramayanmardi@gmail.com
version: 1.0.0
requirements: Tkinter
'''

'''
This script is main script of the 'TileMapEditor Software'. This file
controls/runs the whole software. This script helps in assembling all the other component
needed for the software to run.

Module Contain: ["TileMapEditor"]
    class: `TileMapEditor`:- Operate the software.
'''

import tkinter as tk
# component contain all the other element need for the software (i.e widget, support files.)
from component import (Menu, StatusBar, FileInfoBar)
''''component.utils' contain the supported function which are needed in point of time,
by all other class and also contain CONSTANT for the software.
'''
from component.utils import create_new_project


class TileMapEditor:
    '''class: Controls the software and assemble the software
       :method bind_event: Bind the Keyboard shortcuts and event to the root widget.
       :method add: Assemble and create new widget for the software.
       :method run: Run the software.
    '''

    def __init__(self):
        self.root = tk.Tk()
        # Always appear in the full screen mode of the user device.
        w, h = [self.root.winfo_screenwidth(), self.root.winfo_screenheight()]
        self.root.geometry(f"{w}x{h}+0+0")
        self.root.title("TileMapEditor")

        '''Variable store the current active canvas object which is being worked on.
            It's help in closing and accessing the current using canvas by the whole
            software.
        '''
        self.current_focused_canvas = None

    def __str__(self):
        return f"""TkVersion: {tk.TkVersion}, TileMapEditorVersion: 0.01"""

    def bind_event(self):
        ''':method: bind the event to the root widget for the software. This event
            works all over the software. In any point of time
        '''

        # events for closing the window
        self.root.bind("<Escape>", lambda *args: self.root.destroy())
        self.root.bind("<Control-KeyPress-q>", lambda *args: self.root.destroy())
        # self.root.bind("<>", lambda *args: ProjectInfo(self, self.root))

    def add(self):
        ''':method: assemble all the other component and create some new widget needed
            for the software.
        '''
        # creating frames
        '''Left Frame Hold's the widgets that display the information related to the current
            project. And widgets used to edit the current project.
        '''
        left_frame = tk.Frame(self.root)
        left_frame.place(relx=0, rely=0, relwidth=0.2, relheight=0.96)
        '''Mid Frame Hold's the Canvas (Working Place) and the Canvas Name and stuff
        '''
        mid_frame = tk.Frame(self.root)
        mid_frame.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.96)
        '''Right Frame Hold's the Layer's Related Info as well as spreadsheets.
        '''
        right_frame = tk.Frame(self.root)
        right_frame.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.96)

        # creating widgets
        '''`FileInforBar` Widget display the current file name and can used for,
            focusing and destroying the current project.
        '''
        self.fileinfobar = FileInfoBar(self, mid_frame, background="#5F40E8")
        self.fileinfobar.place(relx=0, rely=0, relwidth=1.0, relheight=0.04)
        '''As variable named it hold the canvas children of the mid frame.
        '''
        self.canvas_frame = tk.Frame(mid_frame, background="grey")
        self.canvas_frame.place(relx=0, rely=0.04, relwidth=1.0, relheight=0.96)

        create_new_project(self, self.canvas_frame, background="grey")
        self.current_focused_canvas = self.canvas_frame.winfo_children()[0]

        '''`Menu` of the software.'''
        Menu(self, self.root)
        '''`StatusBar` Situated all the widgets(Canvas, InfoBar..) to show the some info
            related to the project (i.e Coordinate, Zoom Level etc.)
        '''
        StatusBar(self, self.root,
                  height=0.1).place(relx=0, rely=0.96, relwidth=1.0, relheight=0.04)

    def run(self):
        ''':method: runs the software.'''
        self.add()
        self.bind_event()
        self.root.mainloop()


if __name__ == '__main__':
    TileMapEditor().run()
