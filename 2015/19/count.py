def gen_symbols(molecule):
    pos = 0
    while pos < len(molecule):
        if pos < len(molecule) - 1 and molecule[pos + 1].islower():
            yield molecule[pos : pos + 2]
            pos += 2
        else:
            yield molecule[pos]
            pos += 1


def main():
    with open("replacements.txt") as f:
        molecule = [line.strip() for line in f][-1]

    n_replacements = 0
    for symbol in gen_symbols(molecule):
        n_replacements += 1
        if symbol in ("Rn", "Ar"):
            n_replacements -= 1
        elif symbol == "Y":
            n_replacements -= 2
    n_replacements -= 1
    print(n_replacements)


if __name__ == "__main__":
    main()
