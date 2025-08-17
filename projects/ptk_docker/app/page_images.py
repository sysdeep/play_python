import tkinter as tk
from tkinter import ttk

import pprint

from docker import DockerClient


class PageImages(tk.Frame):
    def __init__(self, parent, docker: DockerClient, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._docker = docker

        tk.Label(self, text="hello").pack()

        # tree
        tree_columns = [
            "tag",
            "size",
        ]
        self._tree = ttk.Treeview(
            self,
            show="tree headings",
            selectmode="browse",
            columns=tree_columns,
        )
        self._tree.pack(side="left", expand=True, fill="both")

        self._tree.heading("#0", text="id")
        self._tree.heading("tag", text="Tag")
        self._tree.heading("size", text="Size")

        self._tree.column("#0", minwidth=200, width=200)
        # self._tree.column("id", minwidth=90, width=90)

        # vertical scroll
        ysb = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
        self._tree["yscroll"] = ysb.set
        ysb.pack(side="right", expand=False, fill="y", anchor="e")

        # self._tree.column("#0", width=300)
        self._tree.tag_bind("simple", "<<TreeviewSelect>>", self._select_row)
        self._tree.bind("<Double-1>", self._open_row)
        # self._tree.tag_bind("simple", "<<TreeviewOpen>>", self.__open_row)
        self._tree.bind("<Button-3>", self._make_cmenu)

        self.cmenu = tk.Menu(self, tearoff=0)
        self.cmenu.add_command(
            label="Свойства",
            command=self._show_info,
            # image=ticons.ticon(ticons.INFO),
            compound="left",
        )
        # self.cmenu.add_command(label="Экспорт", command=self.__show_export, image=ticons.ticon(ticons.I_EXPORT), compound="left")
        self.cmenu.add_command(
            label="Удалить",
            command=self._show_remove,
            # image=ticons.ticon(ticons.TRASH),
            compound="left",
        )

        # start
        self._fill_table()

    def _fill_table(self):

        # clear
        for row in self._tree.get_children():
            self._tree.delete(row)

        all_images = self._docker.images.list()

        for img in all_images:
            pprint.pprint(img.attrs)

            ivalues = (
                img.tags[0] if img.tags else "-",
                # "\n".join(img.tags),
                img.attrs.get("Size", 0),
            )

            self._tree.insert(
                "",
                "end",
                img.short_id,
                text=img.short_id,
                # tags=("simple",),
                # image=icon,
                values=ivalues,
            )

    def _select_row(self, e):
        print("select")

    def _open_row(self, e):
        print("open")

    def _make_cmenu(self, e):
        cmenu_selection = self._tree.identify_row(e.y)  # тек. елемент под курсором

        if cmenu_selection:
            self._tree.selection_set(cmenu_selection)  # выделяем его

            # автозакрытие при потере фокуса(https://stackoverflow.com/questions/21200516/python3-tkinter-popup-menu-not-closing-automatically-when-clicking-elsewhere)
            self.cmenu.tk_popup(e.x_root, e.y_root)

    def _show_info(self):
        print("show info")

    def _show_remove(self):
        print("show remove")
