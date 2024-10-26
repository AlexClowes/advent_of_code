from collections import defaultdict
import re


def main():
    with open("scratchcards.txt") as f:
        card_counts = defaultdict(int)
        for card_no, line in enumerate(f, 1):
            card_counts[card_no] += 1
            winning_nos, my_nos = map(
                lambda nos: [int(n) for n in nos.split()],
                re.match(
                    r"Card +(?:\d+): ([\d ]+) \| ([\d ]+)", line.strip()
                ).groups(),
            )
            matches = sum(my_no in winning_nos for my_no in my_nos)
            for card in range(card_no + 1, card_no + matches + 1):
                card_counts[card] += card_counts[card_no]
    print(sum(card_counts.values()))


if __name__ == "__main__":
    main()
