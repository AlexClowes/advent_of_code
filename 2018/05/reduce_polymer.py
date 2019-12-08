def react(polymer):
    reduced = [" "]
    for char in polymer:
        if abs(ord(char) - ord(reduced[-1])) == 32:
            reduced.pop()
        else:
            reduced.append(char)
    return "".join(reduced[1:])


def main():
    with open("polymer.txt") as f:
        polymer = f.read().strip()

    # Part 1
    reduced_poly = react(polymer)
    print(len(reduced_poly))

    # Part 2
    new_polys = (
        reduced_poly.replace(char, "").replace(char.upper(), "")
        for char in "abcdefghijklmnopqrstuvwxyz"
    )
    print(min(len(react(poly)) for poly in new_polys))


if __name__ == "__main__":
    main()
