def is_possible(side_lens):
    side_lens = sorted(side_lens)
    return side_lens[2] < side_lens[0] + side_lens[1]


def main():
    with open("triangles.txt") as f:
        side_lens = (map(int, line.split()) for line in f)
        print(sum(is_possible(sl) for sl in side_lens))


if __name__ == "__main__":
    main()
