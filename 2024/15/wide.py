CHAR2MOVE = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def main():
    with open("input.txt") as f:
        blocks = set()
        boxes = set()
        for i, line in enumerate(f):
            if not line.strip():
                break
            for j, char in enumerate(line.strip()):
                if char == "@":
                    robot_pos = (i, 2 * j)
                elif char == "#":
                    blocks.add((i, 2 * j))
                    blocks.add((i, 2 * j + 1))
                elif char == "O":
                    boxes.add((i, 2 * j))
                elif char == ".":
                    pass
                else:
                    raise ValueError(f"Unexpected char {char}")

        moves = [CHAR2MOVE[char] for line in f for char in line.strip()]

    for move in moves:
        move_fn = lambda pos: (pos[0] + move[0], pos[1] + move[1])

        new_robot_pos = move_fn(robot_pos)
        if new_robot_pos in blocks:
            continue

        boxes_moved = {new_robot_pos, (new_robot_pos[0], new_robot_pos[1] - 1)} & boxes
        just_moved = new_box_positions = {move_fn(box) for box in boxes_moved}
        while just_moved:
            displaced = set.union(
                *({(i, j - 1), (i, j), (i, j + 1)} for i, j in just_moved),
            ) - boxes_moved & boxes
            boxes_moved.update(displaced)
            just_moved = {move_fn(box) for box in displaced}
            new_box_positions.update(just_moved)

        if not any({(i, j), (i, j + 1)} & blocks for i, j in new_box_positions):
            robot_pos = new_robot_pos
            boxes = boxes - boxes_moved | new_box_positions

    print(sum(100 * i + j for i, j in boxes))


if __name__ == "__main__":
    main()
