from typing import Optional

from app.storage.node import Node


class Tree:

    def __init__(self):
        self._root = Node(None, 0)
        # self._current_node = self._root

    # def append(self, b: int) -> AppendResult:
    #
    #     node = self._current_node.find_tree_node(b)
    #
    #     if node:
    #         self._current_node = node
    #         return AppendResult(id(node), False)
    #
    #     new_node = Node(self._current_node, b)
    #
    #     self._current_node = self._root
    #
    #     return AppendResult(id(new_node), True)
    #
    # def get_write_worker(self) -> WriteWorker:
    #     return WriteWorker(self)
    #
    # def get_read_worker(self) -> ReadWorker:
    #     return ReadWorker(self)

    def get_root(self) -> Node:
        return self._root

    def get_node(self, node_id: int) -> Node:

        def re_find(node: Node, node_id) -> Optional[Node]:
            if id(node) == node_id:
                return node

            for n in node.childrens:
                res = re_find(n, node_id)
                if res:
                    return res

            return None

        nn = re_find(self._root, node_id)

        return nn

    def get_path_data(self, node: Node) -> bytes:

        self_data = node.data.to_bytes(1, 'big')

        if node.parent:
            parent_data = self.get_path_data(node.parent)

            return parent_data + self_data

        return b''
