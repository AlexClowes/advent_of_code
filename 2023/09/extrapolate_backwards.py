def extrapolate(sequence):
    if all(n == 0 for n in sequence):
        return 0
    diffs = [a - b for a, b in zip(sequence[1:], sequence)]
    return sequence[0] - extrapolate(diffs)


def main():
    with open("report.txt") as f:
        observations = ([int(n) for n in line.strip().split()] for line in f)
        print(sum(extrapolate(observation) for observation in observations))


if __name__ == "__main__":
    main()
