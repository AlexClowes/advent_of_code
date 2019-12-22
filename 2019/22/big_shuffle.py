from small_shuffle import shuffle


def main():
    with open("instructions.txt") as f:
        instructions = [line.strip() for line in f]

    repeats = 101741582076661
    deck_len = 119315717514047
    card_no = 2020

    b = shuffle(instructions, 0, deck_len)
    a = (shuffle(instructions, 1, deck_len) - b) % deck_len

    print(
        (
            pow(a, deck_len - repeats - 1, deck_len) * card_no
            - b
            * (pow(a, deck_len - repeats - 1, deck_len) - 1)
            * pow(1 - a, deck_len - 2, deck_len)
        )
        % deck_len
    )


if __name__ == "__main__":
    main()
