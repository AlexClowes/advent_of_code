from math import prod


def main():
    with open("problems.txt") as f:
        lines = [line[:-1] + " " for line in f]

    digit_gen = zip(*lines[:-1])
    operators = (sum if symbol == "+" else prod for symbol in lines[-1].split())

    total = 0
    for operator in operators:
        operands = []
        while True:
            digits = next(digit_gen)
            if all(digit == " " for digit in digits):
                break
            operands.append(int("".join(digits)))
        total += operator(operands)
    print(total)


if __name__ == "__main__":
    main()
