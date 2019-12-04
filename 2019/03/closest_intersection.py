def build_path(instructions):
    path = {(0, 0)}
    current_pos = (0, 0)
    for instr in instructions:
        direction = instr[0]
        distance = int(instr[1:])
        if direction == "U":
            path |= {(current_pos[0], current_pos[1] + i + 1) for i in range(distance)}
            current_pos = (current_pos[0], current_pos[1] + distance)
        elif direction == "D":
            path |= {(current_pos[0], current_pos[1] - i - 1) for i in range(distance)}
            current_pos = (current_pos[0], current_pos[1] - distance)
        elif direction == "R":
            path |= {(current_pos[0] + i + 1, current_pos[1]) for i in range(distance)}
            current_pos = (current_pos[0] + distance, current_pos[1])
        elif direction == "L":
            path |= {(current_pos[0] - i - 1, current_pos[1]) for i in range(distance)}
            current_pos = (current_pos[0] - distance, current_pos[1])
    return path


def manhattan_metric(pos):
    return abs(pos[0]) + abs(pos[1])


def main():
    with open("instructions.txt") as f:
        path1 = build_path(f.readline().split(","))
        path2 = build_path(f.readline().split(","))

    intersections = path1 & path2 - {(0, 0)}
    print(min(map(manhattan_metric, intersections)))


if __name__ == "__main__":
    main()
