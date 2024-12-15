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
                    robot_pos = (i, j)
                elif char == "#":
                    blocks.add((i, j))
                elif char == "O":
                    boxes.add((i, j))
                elif char == ".":
                    pass
                else:
                    raise ValueError(f"Unexpected char {char}")

        moves = [CHAR2MOVE[char] for line in f for char in line.strip()]

    for di, dj in moves:
        new_robot_pos = would_move = (robot_pos[0] + di, robot_pos[1] + dj)
        boxes_to_move = set()
        new_box_positions = set()
        while would_move in boxes:
            boxes_to_move.add(would_move)
            would_move = (would_move[0] + di, would_move[1] + dj)
            new_box_positions.add(would_move)
        if would_move not in blocks:
            robot_pos = new_robot_pos
            boxes = boxes - boxes_to_move | new_box_positions

    print(sum(100 * i + j for i, j in boxes))


if __name__ == "__main__":
    main()
