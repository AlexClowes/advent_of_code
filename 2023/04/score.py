import re


def score(winning_nos, my_nos):
    ret = 0
    for no in my_nos:
        if no in winning_nos:
            if ret == 0:
                ret = 1
            else:
                ret *= 2
    return ret


def main():
    with open("scratchcards.txt") as f:
        total = 0
        for line in f:
            winning_nos, my_nos = map(
                lambda nos: [int(n) for n in nos.split()],
                re.match(
                    r"Card +(?:\d+): ([\d ]+) \| ([\d ]+)", line.strip()
                ).groups(),
            )
            total += score(winning_nos, my_nos)
        print(total)


if __name__ == "__main__":
    main()
