def get_cards(f):
    assert f.readline().startswith("Player")
    while line := f.readline().strip():
        yield int(line)


def main():
    with open("cards.txt") as f:
        deck1 = tuple(get_cards(f))
        deck2 = tuple(get_cards(f))

    def recursive_combat(deck1, deck2):
        seen = set()
        while deck1 and deck2:
            if (deck1, deck2) in seen:
                return True, deck1
            seen.add((deck1, deck2))

            card1, deck1 = deck1[0], deck1[1:]
            card2, deck2 = deck2[0], deck2[1:]
            if len(deck1) >= card1 and len(deck2) >= card2:
                deck1_wins, _ = recursive_combat(deck1[:card1], deck2[:card2])
            else:
                deck1_wins = card1 > card2

            if deck1_wins:
                deck1 = deck1 + (card1, card2)
            else:
                deck2 = deck2 + (card2, card1)

        return bool(deck1), deck1 or deck2

    _, winning_deck = recursive_combat(deck1, deck2)
    print(sum(n * card for n, card in enumerate(reversed(winning_deck), 1)))


if __name__ == "__main__":
    main()
