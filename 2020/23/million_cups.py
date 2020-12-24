from itertools import chain


class Node:
    def __init__(self, val, lookup):
        self.val = val
        lookup[val] = self


def main():
    # Buid circular linked list
    start_cups = "871369452"
    cup_vals = [int(n) for n in start_cups]
    cup_vals = chain(cup_vals, range(max(cup_vals) + 1, 10 ** 6 + 1))
    cup_lookup = {}
    node = first_node = Node(next(cup_vals), lookup=cup_lookup)
    for val in cup_vals:
        node.next = Node(val, lookup=cup_lookup)
        node = node.next
    node.next = first_node

    # Get min and max cup vals
    max_cup = 10 ** 6

    # Play the cup game
    current_cup = first_node
    for _ in range(10 ** 7):
        # Remove three cups after current cup
        three_cups = current_cup.next
        current_cup.next = current_cup.next.next.next.next

        # Get label of destination cup
        dest = current_cup.val - 1 or max_cup
        while dest in (three_cups.val, three_cups.next.val, three_cups.next.next.val):
            dest = dest - 1 or max_cup
        dest_cup = cup_lookup[dest]

        # Place 3 cups after destination cup
        three_cups.next.next.next = dest_cup.next
        dest_cup.next = three_cups

        # Get new current cup
        current_cup = current_cup.next

    print(cup_lookup[1].next.val * cup_lookup[1].next.next.val)


if __name__ == "__main__":
    main()
