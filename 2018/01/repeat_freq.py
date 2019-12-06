from itertools import cycle


def main():
    with open("freq_changes.txt") as f:
        changes = cycle(int(line) for line in f)
        val = 0
        prev_vals = set()
        for change in changes:
            val += change
            if val in prev_vals:
                print(val)
                break
            else:
                prev_vals.add(val)


if __name__ == "__main__":
    main()
