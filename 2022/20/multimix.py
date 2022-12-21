class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class File:
    def __init__(self, nodes):
        nodes[0].prev = nodes[-1]
        nodes[-1].next = nodes[0]
        for n1, n2 in zip(nodes, nodes[1:]):
            n1.next = n2
            n2.prev = n1
        self.nodes = nodes

        assert sum(node.val == 0 for node in self.nodes) == 1

    def __iter__(self):
        node = start = self.nodes[0]
        yield node
        node = node.next
        while node is not start:
            yield node
            node = node.next

    def move(self, node):
        # import pdb; pdb.set_trace()
        dest = node
        if node.val > 0:
            for _ in range(node.val % (len(self) - 1)):
                dest = dest.next
        else:
            for _ in range((-node.val + 1) % (len(self) - 1)):
                dest = dest.prev
        # Remove from list
        node.prev.next, node.next.prev = node.next, node.prev

        # Add back in after dest
        dest_next = dest.next
        dest.next = dest_next.prev = node
        node.prev = dest
        node.next = dest_next

    def mix(self):
        for node in self.nodes:
            self.move(node)

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, idx):
        node = next(node for node in self if node.val == 0)
        for _ in range(idx % len(self)):
            node = node.next
        return node


def main():
    decryption_key = 811589153
    with open("file.txt") as f:
        file = File([Node(decryption_key * int(line.strip())) for line in f])

    for _ in range(10):
        file.mix()
    print(sum(file[idx].val for idx in (1000, 2000, 3000)))


if __name__ == "__main__":
    main()
