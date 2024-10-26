from collections import Counter
from enum import IntEnum


Card = IntEnum("Card", list("J23456789TQKA"))
    
Type = IntEnum(
    "Type",
    [
        "HighCard",
        "OnePair",
        "TwoPair",
        "ThreeOfAKind",
        "FullHouse",
        "FourOfAKind",
        "FiveOfAKind",
    ]
)


def get_type(hand):
    # Convert jokers to most common non-joker card in deck
    try:
        most_common_non_joker = Counter(
            card for card in hand if card is not Card.J
        ).most_common(1)[0][0]
        hand = tuple(
            most_common_non_joker if card is Card.J else card for card in hand
        )
    except IndexError:
        # All cards are jokers
        pass

    card_counts = tuple(count for _, count in Counter(hand).most_common())

    if card_counts == (5,):
        return Type.FiveOfAKind
    if card_counts == (4, 1):
        return Type.FourOfAKind
    if card_counts == (3, 2):
        return Type.FullHouse
    if card_counts == (3, 1, 1):
        return Type.ThreeOfAKind
    if card_counts == (2, 2, 1):
        return Type.TwoPair
    if card_counts == (2, 1, 1, 1):
        return Type.OnePair
    return Type.HighCard


def rank_hand(hand):
    return (get_type(hand), *hand)


def main():
    with open("hands.txt") as f:
        hand2bid = {}
        for line in f:
            hand_str, bid_str = line.strip().split()
            hand2bid[tuple(Card[card] for card in hand_str)] = int(bid_str)

    print(
        sum(
            rank * hand2bid[hand]
            for rank, hand in enumerate(
                sorted(hand2bid.keys(), key=rank_hand), 1,
            )
        )
    )


if __name__ == "__main__":
    main()
