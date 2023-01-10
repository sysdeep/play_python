from app.storage.tree import Tree
from app.storage.sequence_reader import SequenceReader
from app.storage.sequence_writer import SequenceWriter


class Container:

    def __init__(self, tree: Tree):
        self._tree = tree
        self._seq = []

    def pack_data(self, data: bytes):

        self._seq = []
        worker = SequenceWriter(self._tree)

        last_result = None
        for b in data:
            res = worker.append(b)
            if res.is_eop:
                self._seq.append(res.node_id)

            last_result = res

        # если закончили, и последняя операция - не вставка новой ноды, фиксируем id ноды
        if last_result and last_result.is_eop is False:
            self._seq.append(last_result.node_id)

    def unpack_data(self) -> bytes:
        worker = SequenceReader(self._tree)

        result = b''
        for node_id in self._seq:
            bdata = worker.get_chunk(node_id)

            result += bdata

        return result
