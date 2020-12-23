from collections import deque


def rotate(cups):
    cups.append(cups.popleft())


def main():
    cups = deque(map(int, "871369452"))
    max_cup = max(cups)
    min_cup = min(cups)

    for _ in range(100):
        current_cup = cups[0]

        # Remove three cups after current cup
        rotate(cups)
        three_cups = (cups.popleft(), cups.popleft(), cups.popleft())

        # Get label of destination cup
        dest = current_cup - 1 if current_cup > min_cup else max_cup
        while dest in three_cups:
            dest = dest - 1 if dest > min_cup else max_cup

        # Place three cups after destination cup
        while cups[-1] != dest:
            rotate(cups)
        cups.extend(three_cups)

        # Move cups so next current cup is correct
        while cups[-1] != current_cup:
            rotate(cups)

    while cups[-1] != 1:
        rotate(cups)
    cups.pop()
    print("".join(map(str, cups)))


if __name__ == "__main__":
    main()
