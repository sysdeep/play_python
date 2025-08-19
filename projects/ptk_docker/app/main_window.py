import tkinter as tk
from tkinter import ttk

from docker import DockerClient

from app.ui.page_images.page_images import PageImages

# from .page_images import PageImages
from .page_containers import PageContainers


class MainWindow(tk.Tk):
    def __init__(
        self,
        docker: DockerClient,
        screenName=None,
        baseName=None,
        className="Tk",
        useTk=True,
        sync=False,
        use=None,
    ):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title("Tkinter docker")
        self.minsize(800, 400)

        # tabs
        tabs = ttk.Notebook(self)
        tabs.pack(expand=True, fill="both", padx=10, pady=10)

        # page containers
        page_containers = PageContainers(tabs)
        tabs.add(page_containers, text="Containers")

        # page images
        page_images = PageImages(tabs, docker=docker)
        tabs.add(page_images, text="Images")

        # page_images2 = PageImages(tabs)
        # tabs.add(page_images2, text="Tab Two")
        # page_images.pack()

        tabs.select(page_images)
