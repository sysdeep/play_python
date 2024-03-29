"""
https://stackoverflow.com/questions/21420447/need-help-in-adding-binary-numbers-in-python
"""
import struct

# a = "hello"
# b = "world"

# result = []
# for i, _ in enumerate(a.encode()):
#     aa = a[len(a) - i - 1]
#     bb = b[len(b) - i - 1]
#
#     print(aa + bb)
#


def add(acc: bytes, value: bytes) -> bytes:

    # carry = 0

    a = struct.unpack("<B", acc)[0]
    b = struct.unpack("<B", value)[0]

    print('add: ', a, b)
    r = a + b

    return struct.pack("<H", r)


def push_to_store(store: bytearray, v: bytes):

    i = 0
    cv = v
    while True:
        if len(store) < i + 1:
            store.append(0)

        a = store[i:i + 1]
        print('aaa: ', a)

        add_result = add(a, cv)

        p, c = struct.unpack("<BB", add_result)

        print('add result: ', p, c)

        if c:
            # add to acc
            pass
            i += 1
            cv = c.to_bytes(1, 'little')
        else:

            store[i] = p
            break


def pack(store: bytearray, payload: bytes):
    for i, _ in enumerate(payload):
        b = payload[i:i + 1]
        push_to_store(store, b)


# store = bytearray(b'\x00')
store = bytearray(0)

# push_to_store(store, b'\xff')
# push_to_store(store, b'\x01')
# push_to_store(store, b'\xff')
# push_to_store(store, b'\xff')


def unpack(store: bytearray, v: bytes):
    result = bytearray()

    i = 0
    while store:
        b = store[i:i + 1]
        print(b)

        b1, b2 = struct.unpack('<H', b)

        v1 = struct.unpack('<B', v)[0]
        print(b, b1, b2, v1)
        break
        # r1 = b1 - v1


if __name__ == "__main__":

    pack(store, b'1234')

    print(store)
    # unpack(store, b'4')
