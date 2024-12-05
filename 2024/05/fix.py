from itertools import takewhile


def find(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return -1


def fixed(update, rules):
    had_to_fix = False
    done = False
    while not done:
        done = True
        for first, second in rules:
            if (
                (fst_idx := find(update, first)) != -1
                and (snd_idx := find(update, second)) != -1
                and fst_idx > snd_idx
            ):
                update[fst_idx], update[snd_idx] = update[snd_idx], update[fst_idx]
                done = False
                had_to_fix = True
    return had_to_fix


def median(update):
    assert len(update) % 2 == 1
    return update[len(update) // 2]


def main():
    with open("print_orders.txt") as f:
        rule_lines = takewhile(bool, (line.strip() for line in f))
        rules = [line.split("|") for line in rule_lines]
        updates = [line.strip().split(",") for line in f]

    print(sum(int(median(update)) for update in updates if fixed(update, rules)))


if __name__ == "__main__":
    main()
