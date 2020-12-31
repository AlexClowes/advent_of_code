import re


def dist(pos1, pos2):
    return sum(abs(x1 - x2) for x1, x2 in zip(pos1, pos2))


def main():
    with open("nanobots.txt") as f:
        nanobots = [tuple(map(int, re.findall(r"-?\d+", line))) for line in f]

    *strongest_pos, strongest_rad = max(nanobots, key=lambda t: t[3])
    print(sum(dist(bot[:3], strongest_pos) <= strongest_rad for bot in nanobots))


if __name__ == "__main__":
    main()
