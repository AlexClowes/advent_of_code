from collections import defaultdict


def main():
    with open("elves.txt") as f:
        positions = {
            (i, j)
            for i, line in enumerate(f)
            for j, char in enumerate(line.strip())
            if char == "#"
        }

    def check_empty(to_check):
        return all(pos not in positions for pos in to_check)

    headings = [
        (
            (-1, 0),
            lambda i, j: check_empty((i - 1, j + dj) for dj in (-1, 0, 1)),
        ),
        (
            (1, 0),
            lambda i, j: check_empty((i + 1, j + dj) for dj in (-1, 0, 1)),
        ),
        (
            (0, -1),
            lambda i, j: check_empty((i + di, j - 1) for di in (-1, 0, 1)),
        ),
        (
            (0, 1),
            lambda i, j: check_empty((i + di, j + 1) for di in (-1, 0, 1)),
        ),
    ]

    def get_move(i, j):
        moves = defaultdict(list)
        if not check_empty(
            (i + di, j + dj)
            for di in (-1, 0, 1)
            for dj in (-1, 0, 1)
            if di != 0 or dj != 0
        ):
            for (di, dj), condition in headings:
                if condition(i, j):
                    return i + di, j + dj
        return i, j

    def iterate():
        nonlocal positions

        desired_moves = defaultdict(list)
        for pos in positions:
            desired_moves[get_move(*pos)].append(pos)

        elf_moved = False
        new_positions = set()
        for move, candidates in desired_moves.items():
            if len(candidates) == 1:
                new_positions.add(move)
                if move != candidates[0]:
                    elf_moved = True
            else:
                new_positions.update(candidates)
        positions = new_positions
        headings.append(headings.pop(0))

        return elf_moved

    for _ in range(10):
        iterate()

    ymin = min(i for i, _ in positions)
    ymax = max(i for i, _ in positions)
    xmin = min(j for _, j in positions)
    xmax = max(j for _, j in positions)
    print((ymax - ymin + 1) * (xmax - xmin + 1) - len(positions))


if __name__ == "__main__":
    main()
