from typing import Optional, List


class Node:

    def __init__(self, parent: Optional['Node'], data: int):
        self.data = data
        self.parent = parent
        self.childrens: List['Node'] = []

        if self.parent:
            self.parent.childrens.append(self)

    def find_tree_node(self, b: int) -> Optional['Node']:
        for node in self.childrens:
            if node.data == b:
                return node

        return None



    # moved to tree
    # def get_path_data(self) -> bytes:

    #     self_data = self.data.to_bytes(1, 'big')

    #     if self.parent:
    #         parent_data = self.parent.get_path_data()

    #         return parent_data + self_data


    #     return b''