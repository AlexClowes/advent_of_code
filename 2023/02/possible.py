from collections import defaultdict
import re


def max_by_colour(cube_counts):
    ret = defaultdict(int)
    for draw in cube_counts.split("; "):
        for count_colour in draw.split(", "):
            count, colour = count_colour.split(" ")
            ret[colour] = max(ret[colour], int(count))
    return ret


def is_possible(cube_counts, limit):
    return all(
        colour in limit and count <= limit[colour]
        for colour, count in max_by_colour(cube_counts).items()
    )


def main():
    limit = dict(red=12, green=13, blue=14)
    total = 0
    with open("games.txt") as f:
        for line in f:
            game_id, cube_counts = re.match(r"Game (\d+): (.*)\n", line).groups()
            if is_possible(cube_counts, limit):
                total += int(game_id)
        print(total)


if __name__ == "__main__":
    main()
