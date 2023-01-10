import hashlib
import os.path

from app.container import Container
from app.storage.tree import Tree
import pytest


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


def test_container_file():

    self_path = os.path.abspath(__file__)
    unpack_path = '/tmp/test_file'

    t = Tree()
    c = Container(t)

    with open(self_path, 'rb') as fd:
        c.pack_data(fd.read())

    with open(unpack_path, 'wb') as fd:
        fd.write(c.unpack_data())

    assert file_md5(self_path) == file_md5(unpack_path)


def file_md5(fname: str):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
