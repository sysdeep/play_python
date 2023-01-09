from typing import Optional
from node import Node


class Tree:

    def __init__(self):
        self._root = Node(None, b'')
        self._current_node = self._root

    def append(self, b: bytes) -> int:

        node = self._current_node.find_tree_node(b)

        if node:
            self._current_node = node
            return -1

        new_node = Node(self._current_node, b)

        self._current_node = self._root

        return id(new_node)


if __name__ == "__main__":

    tree = Tree()
    # for b in b'Hello':
    v = tree.append(b'H')
    print(v)
