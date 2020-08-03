def incr(characters):
    for i, c in enumerate(characters[::-1]):
        if c == "z":
            characters[-1 - i] = "a"
        else:
            characters[-1 - i] = chr(ord(c) + 1)
            break


def run_of_three(characters):
    for i in range(len(characters) - 2):
        if ord(characters[i]) == ord(characters[i + 1]) - 1 == ord(characters[i + 2]) - 2:
            return True
    return False


def two_doubles(characters):
    prev_double = ""
    doubles = 0
    for c1, c2 in zip(characters[:-1], characters[1:]):
        if c1 == c2 != prev_double:
            doubles += 1
            prev_double = c1
            if doubles == 2:
                return True
    return False


def no_banned_letters(characters):
    return all(c not in "iol" for c in characters)

def allowed(characters):
    return no_banned_letters(characters) and two_doubles(characters) and run_of_three(characters)


def main():
    characters = list("cqjxjnds")
    while not allowed(characters):
        incr(characters)
    print("".join(characters))

    incr(characters)
    while not allowed(characters):
        incr(characters)
    print("".join(characters))


if __name__ == "__main__":
    main()
