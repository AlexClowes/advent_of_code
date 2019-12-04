def build_path(instructions):
    path = {}
    current_pos = (0, 0)
    path_length = 0
    for instr in instructions:
        direction = instr[0]
        distance = int(instr[1:])
        if direction == "U":
            path.update({
                (current_pos[0], current_pos[1] + i): path_length + i
                for i in range(1, distance + 1)
            })
            current_pos = (current_pos[0], current_pos[1] + distance)
            path_length += distance
        elif direction == "D":
            path.update({
                (current_pos[0], current_pos[1] - i): path_length + i
                for i in range(1, distance + 1)
            })
            current_pos = (current_pos[0], current_pos[1] - distance)
            path_length += distance
        elif direction == "R":
            path.update({
                (current_pos[0] + i, current_pos[1]): path_length + i
                for i in range(1, distance + 1)
            })
            current_pos = (current_pos[0] + distance, current_pos[1])
            path_length += distance
        elif direction == "L":
            path.update({
                (current_pos[0] - i, current_pos[1]): path_length + i
                for i in range(1, distance + 1)
            })
            current_pos = (current_pos[0] - distance, current_pos[1])
            path_length += distance
    return path


def main():
    with open("instructions.txt") as f:
        path1 = build_path(f.readline().split(","))
        path2 = build_path(f.readline().split(","))

    intersection_distances = {path1[k] + path2[k] for k in set(path1) & set(path2)}
    print(min(intersection_distances))




if __name__ == "__main__":
    main()
