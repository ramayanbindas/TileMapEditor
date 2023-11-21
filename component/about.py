''''''
import tkinter as tk


class About(tk.Toplevel):
    def __init__(self, app, parent: tk.Widget, **kw):
        super().__init__(parent, **kw)
        rel_w = round(self.master.winfo_width() * 0.6)
        rel_h = round(self.master.winfo_height() * 0.6)
        x = round((self.master.winfo_width() - rel_w) / 2)
        y = round((self.master.winfo_height() - rel_h) / 2)
        self.geometry(f"{rel_w}x{rel_h}+{x}+{y}")
        self.title("About")

        self.add()
        self.event()

    def add(self):
        text = tk.Text(self)
        text.place(relx=0, rely=0, relwidth=0.99, relheight=1.0)
        text.insert(tk.INSERT, f"TkVersion: {tk.TkVersion}, TileMapEditorVersion: 0.01")
        text.config(state=tk.DISABLED)

        v_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=text.yview)
        v_scrollbar.place(relx=0.99, rely=0, relwidth=0.01, relheight=1.0)
        text.config(yscrollcommand=v_scrollbar.set)

    def event(self):
        self.bind("<Escape>", lambda *args: self.destroy())


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800+0+0")
    tk.Button(text="press me", command=lambda: About(None, root)).pack(side=tk.TOP)
    root.mainloop()
