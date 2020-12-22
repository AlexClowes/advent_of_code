from collections import deque


def main():
    deck1 = deque()
    deck2 = deque()
    with open("cards.txt") as f:
        assert f.readline() == "Player 1:\n"
        while line := f.readline().strip():
            deck1.append(int(line))

        assert f.readline() == "Player 2:\n"
        while line := f.readline().strip():
            deck2.append(int(line))

    while deck1 and deck2:
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if card1 > card2:
            deck1.extend((card1, card2))
        else:
            deck2.extend((card2, card1))

    winning_deck = deck1 or deck2
    print(sum(n * card for n, card in enumerate(reversed(winning_deck), 1)))


if __name__ == "__main__":
    main()
