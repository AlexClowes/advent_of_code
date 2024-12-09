from collections import defaultdict
from itertools import chain, repeat


def find_write_ptr(storage, start, end, space_required):
    for write_ptr in range(start, end + 1):
        file_no, space = storage[write_ptr]
        if file_no is None and space >= space_required:
            return write_ptr


def rearrange(storage):
    write_search_start = defaultdict(int)
    for read_ptr in range(len(storage) - 1, -1, -1):
        file_no, size = storage[read_ptr]
        if file_no is None:
            continue
        write_ptr = find_write_ptr(
            storage, write_search_start[size], read_ptr, size
        )
        if write_ptr is not None:
            write_search_start[size] = write_ptr
            _, space_avail = storage[write_ptr]
            storage[write_ptr] = storage[read_ptr]
            storage[read_ptr] = (None, size)
            if leftover_space := space_avail - size:
                storage.insert(write_ptr + 1, (None, leftover_space))
    return storage


def checksum(storage):
    return sum(
        i * (n or 0)
        for i, n in enumerate(
            chain.from_iterable(
                repeat(file_no, size) for file_no, size in storage
            )
        )
    )


def main():
    with open("diskmap.txt") as f:
        diskmap = [int(n) for n in f.read().strip()]

    storage = []
    is_file = True
    for idx, entry in enumerate(diskmap):
        storage.append((idx // 2 if is_file else None, entry))
        is_file = not is_file

    print(checksum(rearrange(storage)))


if __name__ == "__main__":
    main()
