# import hashlib
import os.path

from app.container_file import ContainerFile
from app.storage.tree import Tree


def test_container_file():

    self_path = os.path.abspath(__file__)
    # unpack_path = '/tmp/test_file'

    t = Tree()
    c = ContainerFile(t)

    seq = c.add_file(self_path)
    # seq = c.add_file('/bin/yelp')     63kb -> 11000 nodes
    # seq = c.add_file('/home/nika/bin/hugo')     # 40Mb - не дождался

    print(seq)
    print(len(seq))

    assert True
    # with open(self_path, 'rb') as fd:
    #     c.pack_data(fd.read())
    #
    # with open(unpack_path, 'wb') as fd:
    #     fd.write(c.unpack_data())
    #
    # assert file_md5(self_path) == file_md5(unpack_path)
    #


# def file_md5(fname: str):
#     hash_md5 = hashlib.md5()
#     with open(fname, "rb") as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             hash_md5.update(chunk)
#     return hash_md5.hexdigest()
