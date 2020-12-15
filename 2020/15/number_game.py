def main():
    start_nums = (19, 0, 5, 1, 10, 13)

    last_seen = {n: i for i, n in enumerate(start_nums[:-1], 1)}
    prev_num = start_nums[-1]
    for turn in range(len(start_nums) + 1, 3 * 10 ** 7 + 1):
        prev_seen = last_seen.get(prev_num)
        last_seen[prev_num] = turn - 1
        if prev_seen:
            prev_num = turn - 1 - prev_seen
        else:
            prev_num = 0

        # Answer to part 1
        if turn == 2020:
            print(prev_num)

    # Answer to part 2
    print(prev_num)


if __name__ == "__main__":
    main()
