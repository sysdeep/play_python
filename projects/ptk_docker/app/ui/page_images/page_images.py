import tkinter as tk
from tkinter import messagebox

from docker import DockerClient

from app.domain.image import Image
from app.ui.page_images.images_list_frame import (ImagesListFrame,
                                                  ImagesListHandler)


class PageImages(tk.Frame, ImagesListHandler):
    def __init__(self, parent, docker: DockerClient, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._docker = docker

        tk.Label(self, text="Images").pack()

        # tree
        self._tree_frame = ImagesListFrame(
            self,
            handler=self,
        )
        self._tree_frame.pack(expand=True, fill="both")

        # controls bar
        self._controls_bar = tk.Frame(self, padx=4, pady=4)
        self._controls_bar.pack(side="bottom", fill="x", expand=False)

        tk.Button(self._controls_bar, text="Refresh", command=self._refresh).pack(
            side="right"
        )

        self._stat_variable = tk.StringVar()
        self._stat_label = tk.Label(
            self._controls_bar, textvariable=self._stat_variable
        ).pack(side="left")

        tk.Label(self._controls_bar, text="[d - remove], [D - force remove]").pack(
            side="left"
        )

        # start
        self._refresh()

    def _refresh(self):

        all_images = self._docker.images.list()

        # set to list
        result = [self.to_img(i) for i in all_images]
        self._tree_frame.set_images(result)

        # update stat
        stat_text = f"Images total: {len(result)}"
        self._stat_variable.set(stat_text)

    @classmethod
    def to_img(cls, img) -> Image:
        return Image(
            uid=img.id.split(":")[1],
            short_uid=img.short_id.split(":")[1],
            tags=[*img.tags],
            size=img.attrs.get("Size", 0),
            created=img.attrs.get("Created", ""),
        )

    # images handler interface ------------------------------------------------
    def remove_image(self, uid: str, force: bool):
        msg = f"Force remove image {uid}?" if force else f"Remove image {uid}?"
        result = messagebox.askquestion(
            title="Confirmation",
            message=msg,
        )
        if result == "yes":
            try:
                self._docker.images.remove(uid, force)
            except Exception as e:
                messagebox.showerror("Error", str(e))

            self._refresh()

    def show_image_info(self, uid: str):
        print("show info for: ", uid)
