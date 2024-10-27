import re


def hash(string):
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val %= 256
    return val


class BoxNode:
    def __init__(self):
        self.next = None


class DataNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class HashMap:
    def __init__(self):
        self.boxes = [BoxNode() for _ in range(256)]

    def __delitem__(self, key):
        box = self.boxes[hash(key)]
        last, curr = box, box.next
        while curr is not None:
            if curr.key == key:
                last.next = curr.next
                return
            last, curr = curr, curr.next

    def __setitem__(self, key, val):
        box = self.boxes[hash(key)]
        last, curr = box, box.next
        while curr is not None:
            if curr.key == key:
                curr.val = val
                return
            last, curr = curr, curr.next
        last.next = DataNode(key, val)


def focusing_power(hash_map):
    total = 0
    for box_idx, box in enumerate(hash_map.boxes, 1):
        slot_idx = 1
        curr = box.next
        while curr is not None:
            total += box_idx * slot_idx * curr.val
            curr = curr.next
            slot_idx += 1
    return total


def main():
    with open("init_sequence.txt") as f:
        hash_map = HashMap()
        for instruction in f.read().strip().split(","):
            if match := re.match("(\w+)-", instruction):
                del hash_map[match.group(1)]
            elif match := re.match("(\w+)=(\d+)", instruction):
                hash_map[match.group(1)] = int(match.group(2))

    print(focusing_power(hash_map))


if __name__ == "__main__":
    main()
