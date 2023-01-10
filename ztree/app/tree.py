from typing import Optional
from dataclasses import dataclass

from app.node import Node


@dataclass
class AppendResult:
    node_id: int
    is_eop: bool  # end of path


class WriteWorker:

    def __init__(self, tree: 'Tree'):
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



class ReadWorker:
    def __init__(self, tree: 'Tree'):
        self._tree = tree
        self._current_node = self._tree.get_root()

    def get_chunk(self, node_id: int) -> bytes:
        
        node = self._tree.get_node(node_id)
        return self._tree.get_path_data(node)


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
    def get_write_worker(self) -> WriteWorker:
        return WriteWorker(self)

    def get_read_worker(self) -> ReadWorker:
        return ReadWorker(self)

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


if __name__ == "__main__":

    tree = Tree()
    worker = tree.get_write_worker()
    for b in b'Hello':
        v = worker.append(b)
        print(v)
