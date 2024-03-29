import struct


def add(a: int, b: int) -> bytes:

    # carry = 0

    # a = struct.unpack("<B", acc)[0]
    # b = struct.unpack("<B", value)[0]
    #
    print('add: ', a, b)
    r = a + b

    return struct.pack("<H", r)


def push_to_store(store: bytearray, v: int):

    i = 0
    cv = v
    while True:
        if len(store) < i + 1:
            store.append(0)

        a = store[i]
        print(f'in store at position {i}: ', a)

        add_result = add(a, cv)

        p, c = struct.unpack("<BB", add_result)

        print('add result: ', p, c)

        store[i] = p

        if c:
            # add to acc
            i += 1
            cv = c
        else:

            # store[i] = p
            break
