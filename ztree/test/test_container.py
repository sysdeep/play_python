import pytest

from app.container import Container
from app.storage.tree import Tree


@pytest.mark.parametrize('dataset', (
    b'1',
    b'12',
    b'13',
    b'Hello',
    b'Hello world',
))
def test_container_simple(dataset):

    t = Tree()
    c = Container(t)

    c.pack_data(dataset)

    res = c.unpack_data()

    assert dataset == res
