def rearrange(storage):
    write_ptr, read_ptr = 0, len(storage) - 1
    while write_ptr < read_ptr:
        if storage[write_ptr] is not None:
            write_ptr += 1
        elif storage[read_ptr] is None:
            read_ptr -= 1
        else:
            storage[write_ptr] = storage[read_ptr]
            storage[read_ptr] = None
    return storage[:write_ptr]


def checksum(storage):
    return sum(i * n for i, n in enumerate(storage))


def main():
    with open("diskmap.txt") as f:
        diskmap = [int(n) for n in f.read().strip()]

    storage = []
    is_file = True
    for idx, entry in enumerate(diskmap):
        storage += [idx // 2 if is_file else None] * entry
        is_file = not is_file

    print(checksum(rearrange(storage)))


if __name__ == "__main__":
    main()
