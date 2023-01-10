from app.tree import Tree


def test_append_one():
    tree = Tree()
    worker = tree.get_write_worker()

    res = worker.append(1)

    assert res.is_eop == True

