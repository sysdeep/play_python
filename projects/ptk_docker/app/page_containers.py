import tkinter as tk
import tkinter.ttk as ttk


class PageContainers(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        tk.Label(self, text="containers").pack()

        self._tree = ttk.Treeview(self)
        self._tree.pack(expand=True, fill="both")
