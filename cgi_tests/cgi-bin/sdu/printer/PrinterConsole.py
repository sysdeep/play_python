from ..PartInfo import PartInfo
from .PrinterInterface import PrinterInterface

class PrinterConsole(PrinterInterface):
    def __init__(self):
        pass

    def print_info(self, part: PartInfo):

        print("dev: {}, mount: {}, fs: {}".format(part.dev, part.mount, part.fs))