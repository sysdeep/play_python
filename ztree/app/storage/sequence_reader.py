from .tree import Tree


class SequenceReader:

    def __init__(self, tree: Tree):
        self._tree = tree
        self._current_node = self._tree.get_root()

    def get_chunk(self, node_id: int) -> bytes:

        node = self._tree.get_node(node_id)
        return self._tree.get_path_data(node)
