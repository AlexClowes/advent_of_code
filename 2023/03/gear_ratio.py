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

    numbers = list(get_numbers())

    total = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "*":
                close_nums = []
                for num, (i_n, j_n), num_len in numbers:
                    if (
                        i_n - 1 <= i <= i_n + 1
                        and j_n - 1 <= j <= j_n + num_len
                    ):
                        close_nums.append(num)
                if len(close_nums) == 2:
                    total += close_nums[0] * close_nums[1]
    print(total)


if __name__ == "__main__":
    main()
