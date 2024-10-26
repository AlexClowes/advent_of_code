def main():
    with open("engine.txt") as f:
        grid = [list(line.strip()) for line in f]

    i_max = len(grid)
    assert len(set(len(row) for row in grid)) == 1
    j_max = len(grid[0])

    def get_numbers():
        # Yield number, coordinate of first digit, and length
        for i, row in enumerate(grid):
            j = 0
            while j < j_max:
                if row[j].isdigit():
                    # Found a number!
                    num = num_len = 0
                    while j + num_len < j_max and row[j + num_len].isdigit():
                        num = 10 * num + int(row[j + num_len])
                        num_len += 1
                    yield num, (i, j), num_len
                    j = j + num_len
                else:
                    j += 1

    def is_part_no(i, j, num_len):
        adj_chars = (
            grid[i + di][j + dj]
            for di in (-1, 0, 1)
            for dj in range(-1, num_len + 1)
            if 0 <= i + di < i_max
            if 0 <= j + dj < j_max
        )
        return not all(adj.isdigit() or adj == "." for adj in adj_chars)

    total = 0
    for num, (i, j), num_len in get_numbers():
        if is_part_no(i, j, num_len):
            total += num
    print(total)


if __name__ == "__main__":
    main()
