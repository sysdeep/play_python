from typing import Optional, List


class Node:

    def __init__(self, parent: Optional['Node'], data: bytes):
        self.data = data
        self.parent = parent
        self.childrens: List['Node'] = []

        if self.parent:
            self.parent.childrens.append(self)

    def find_tree_node(self, b: bytes) -> Optional['Node']:
        for node in self.childrens:
            if node.data == b:
                return node

        return None
