def count_jumps(offsets):
    count = 0
    pos = 0
    while 0 <= pos < len(offsets):
        count += 1
        offsets[pos] += 1
        pos += offsets[pos] - 1
    return count


def main():
    with open("offsets.txt") as f:
        offsets = [int(line.strip()) for line in f]
    print(count_jumps(offsets))


if __name__ == "__main__":
    main()
