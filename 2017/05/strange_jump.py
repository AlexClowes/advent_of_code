def count_jumps(offsets):
    count = 0
    pos = 0
    while 0 <= pos < len(offsets):
        count += 1
        os = offsets[pos]
        offsets[pos] += 1 if offsets[pos] < 3 else -1
        pos += os
    return count


def main():
    with open("offsets.txt") as f:
        offsets = [int(line.strip()) for line in f]
    print(count_jumps(offsets))


if __name__ == "__main__":
    main()
