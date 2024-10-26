from collections import defaultdict
import re


def max_by_colour(cube_counts):
    ret = defaultdict(int)
    for draw in cube_counts.split("; "):
        for count_colour in draw.split(", "):
            count, colour = count_colour.split(" ")
            ret[colour] = max(ret[colour], int(count))
    return ret


def product(iterable):
    p = 1
    for element in iterable:
        p *= element
    return p


def main():
    limit = dict(red=12, green=13, blue=14)
    total = 0
    with open("games.txt") as f:
        for line in f:
            game_id, cube_counts = re.match(r"Game (\d+): (.*)\n", line).groups()
            total += product(max_by_colour(cube_counts).values())
        print(total)


if __name__ == "__main__":
    main()
