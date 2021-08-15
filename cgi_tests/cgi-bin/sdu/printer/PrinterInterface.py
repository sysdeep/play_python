from abc import ABC, abstractmethod
from ..PartInfo import PartInfo


class PrinterInterface(ABC):

    @abstractmethod
    def print_info(self, part: PartInfo):
        pass