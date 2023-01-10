from app.storage.tree import Tree
from app.storage.sequence_writer import SequenceWriter


def test_append_one():
    tree = Tree()
    worker = SequenceWriter(tree)

    res = worker.append(1)

    assert res.is_eop
