from dataclasses import dataclass

from .tree import Tree
from .node import Node


@dataclass
class AppendResult:
    node_id: int
    is_eop: bool  # end of path


class SequenceWriter:

    def __init__(self, tree: Tree):
        self._tree = tree
        self._current_node = self._tree.get_root()

    def append(self, b: int) -> AppendResult:

        node = self._current_node.find_tree_node(b)

        if node:
            self._current_node = node
            return AppendResult(id(node), False)

        new_node = Node(self._current_node, b)

        self._current_node = self._tree.get_root()

        return AppendResult(id(new_node), True)
