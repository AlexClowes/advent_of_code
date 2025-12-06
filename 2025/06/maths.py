from math import prod


def main():
    with open("problems.txt") as f:
        lines = [line.strip().split() for line in f]

    operands = zip(*(map(int, line) for line in lines[:-1]))
    operators = (sum if symbol == "+" else prod for symbol in lines[-1])
    print(sum(operator(operands) for operator, operands in zip(operators, operands)))


if __name__ == "__main__":
    main()
