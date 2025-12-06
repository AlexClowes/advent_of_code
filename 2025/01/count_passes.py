from itertools import pairwise


def gen_positions(instructions):
    position = 50
    for instruction in instructions:
        sign = 1 if instruction[0] == "R" else -1
        distance = int(instruction[1:])
        for _ in range(distance):
            position = (position + sign) % 100
            yield position


def main():
    with open("rotations.txt") as f:
        instructions = (line.strip() for line in f)
        print(sum(pos == 0 for pos in gen_positions(instructions)))


if __name__ == "__main__":
    main()
