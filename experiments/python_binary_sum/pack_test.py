import pytest

from app import add, push_to_store
from pack import add as add2
from pack import push_to_store as push_to_store2


@pytest.mark.parametrize('a, b, result', [
    [0, 0, (0, 0)],
    [0, 1, (1, 0)],
    [0, 0xff, (0xff, 0)],
    [0xff, 0x1, (0, 1)],
    [0xff, 0x2, (1, 1)],
    [0xff, 0x3, (2, 1)],
    [0xff, 0xff, (0xff - 1, 1)],
])
def test_add(a: int, b: int, result):

    r, c = add(a.to_bytes(1, 'little'), b.to_bytes(1, 'little'))

    assert r == result[0]
    assert c == result[1]

    # new variant
    r2, c2 = add2(a, b)

    assert r2 == result[0]
    assert c2 == result[1]


@pytest.mark.parametrize("store, value, result", [
    [b'\x00', 0, b'\x00'],
    [b'\x00', 1, b'\x01'],
    [b'\xff\x00', 0x01, b'\x00\x01'],
    [b'\xff\x00', 0xff, b'\xfe\x01'],
    [b'\xff\x01', 0xff, b'\xfe\x02'],
    [b'\xff\x02', 0xff, b'\xfe\x03'],
])
def test_push(store, value, result):

    ss = bytearray(store)

    push_to_store2(ss, value)

    assert ss == result
