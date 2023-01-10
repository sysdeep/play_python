from typing import List

from app.storage.sequence_writer import SequenceWriter
from app.storage.tree import Tree


class ContainerFile:

    def __init__(self, tree: Tree):
        self._tree = tree
        self._seq = []

    def add_file(self, file_path: str) -> List[int]:

        worker = SequenceWriter(self._tree)

        seq = []

        with open(file_path, 'rb') as fd:

            b = fd.read(1)

            last_result = None
            while b:
                res = worker.append(b[0])
                if res.is_eop:
                    seq.append(res.node_id)

                last_result = res
                b = fd.read(1)

            # если закончили, и последняя операция - не вставка новой ноды, фиксируем id ноды
            if last_result and last_result.is_eop is False:
                seq.append(last_result.node_id)

        return seq

    # def unpack_data(self) -> bytes:
    #     worker = SequenceReader(self._tree)
    #
    #     result = b''
    #     for node_id in self._seq:
    #         bdata = worker.get_chunk(node_id)
    #
    #         result += bdata
    #
    #     return result
