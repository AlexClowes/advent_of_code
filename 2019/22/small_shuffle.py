def shuffle(instructions, card, deck_len):
    for instr in instructions:
        if instr == "deal into new stack":
            card = -card - 1
        elif instr.split()[0] == "cut":
            card -= int(instr.split()[-1])
        elif instr.split()[0] == "deal":
            card *= int(instr.split()[-1])
        card %= deck_len
    return card


def main():
    card = 2019
    deck_len = 10007
    with open("instructions.txt") as f:
        print(shuffle((line.strip() for line in f), card, deck_len))


if __name__ == "__main__":
    main()
