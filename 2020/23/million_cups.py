from itertools import chain


class Node:
    def __init__(self, val, lookup=None, next=None, prev=None):
        self.val = val
        if lookup is not None:
            lookup[val] = self
        self.next = None
        self.prev = prev

    def __repr__(self):
        return f"Node({self.val})"


def main():
    # Buid circular linked list
    start_cups = "871369452"
    cup_vals = [int(n) for n in start_cups]
    cup_vals = chain(cup_vals, range(max(cup_vals) + 1, 10 ** 6 + 1))
    cup_lookup = {}
    node = first_node = Node(next(cup_vals), lookup=cup_lookup)
    for val in cup_vals:
        node.next = Node(val, lookup=cup_lookup, prev=node)
        node = node.next
    node.next = first_node
    first_node.prev = node

    # Get min and max cup vals
    max_cup = 10 ** 6

    # Play the cup game
    current_cup = first_node
    for _ in range(10 ** 7):
        # Remove three cups after current cup
        three_cups = current_cup.next
        current_cup.next = current_cup.next.next.next.next
        current_cup.next.prev = current_cup

        # Get label of destination cup
        dest = current_cup.val - 1 or max_cup
        while dest in (three_cups.val, three_cups.next.val, three_cups.next.next.val):
            dest = dest - 1 or max_cup
        dest_cup = cup_lookup[dest]

        # Place 3 cups after destination cup
        dest_cup.next.prev = three_cups.next.next
        three_cups.next.next.next = dest_cup.next
        dest_cup.next = three_cups
        three_cups.prev = dest_cup

        # Get new current cup
        current_cup = current_cup.next

    print(cup_lookup[1].next.val * cup_lookup[1].next.next.val)


if __name__ == "__main__":
    main()
