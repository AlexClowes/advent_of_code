from collections import defaultdict, deque
import re


def get_stacks(file):
    crate_pattern = r"(\s{4}|\[[A-Z]\])"
    stacks = defaultdict(deque)
    for line in file:
        crates = [
            None if s.isspace() else s[1]
            for s in re.findall(crate_pattern, " " + line)
        ]
        if not any(crates):
            break
        for i, crate in enumerate(crates, 1):
            if crate:
                stacks[i].appendleft(crate)
    return stacks


def get_moves(file):
    move_pattern = r"move (\d+) from (\d) to (\d)"
    for line in file:
        yield map(int, re.match(move_pattern, line).groups())


def main():
    with open("starting_stacks.txt") as f:
        stacks = get_stacks(f)
        next(f)  # Skip blank line
        crane = deque()
        for count, src, dest in get_moves(f):
            for _ in range(count):
                crane.append(stacks[src].pop())
            for _ in range(count):
                stacks[dest].append(crane.pop())
            crane.clear()

    print("".join(stacks[i + 1][-1] for i in range(len(stacks))))


if __name__ == "__main__":
    main()
