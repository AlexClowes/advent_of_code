from collections import deque
from itertools import permutations
import re


def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x


def swap(pword, pos1, pos2):
    pword[pos1], pword[pos2] = pword[pos2], pword[pos1]


def swap_letter(pword, let1, let2):
    swap(pword, pword.index(let1), pword.index(let2))


def rotate(pword, direction, n):
    if direction == "left":
        n *= -1
    n %= len(pword)
    if n:
        pword[:n], pword[n:] = pword[-n:], pword[:-n]


def rotate_weird(pword, letter):
    idx = pword.index(letter)
    rotate(pword, "right", 1 + idx + (idx >= 4))


def reverse(pword, pos1, pos2):
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
    pword[pos1:pos2+1] = pword[pos1:pos2+1][::-1]


def move(pword, pos1, pos2):
    l = pword[pos1]
    del pword[pos1]
    pword.insert(pos2, l)


def scramble(start, instructions):
    operations = {
        r"swap position (\d+) with position (\d+)": swap,
        r"swap letter (\w) with letter (\w)": swap_letter,
        r"rotate (left|right) (\d+) steps?": rotate,
        r"rotate based on position of letter (\w)": rotate_weird,
        r"reverse positions (\d+) through (\d+)": reverse,
        r"move position (\d+) to position (\d+)": move,
    }
    pword = list(start)
    for instr in instructions:
        for pat, op in operations.items():
            m = re.match(pat, instr)
            if m:
                op(pword, *map(try_int, m.groups()))
                break
        else:
            raise ValueError(f"Unable to parse instruction \"{instr}\"")
    return "".join(pword)


def main():
    with open("instructions.txt") as f:
        instructions = f.readlines()

    print(scramble("abcdefgh", instructions))

    for candidate in permutations("abcdefgh"):
        if scramble(candidate, instructions) == "fbgdceah":
            print("".join(candidate))
            break


if __name__ == "__main__":
    main()
