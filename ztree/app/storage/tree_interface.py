from abc import ABC, abstractmethod

from .node import Node


class TreeInterface(ABC):

    @abstractmethod
    def get_root(self) -> Node:
        pass
