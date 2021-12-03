import numpy as np


def binary_to_decimal(bin_array):
    return int("".join(map(str, bin_array)), base=2)


def filter_report(report, criteria):
    bit_idx = 0
    while len(report) > 1:
        ones_count = sum(num[bit_idx] for num in report)
        bit_criteria = criteria(ones_count, report)
        report -= {num for num in report if num[bit_idx] != bit_criteria}
        bit_idx += 1
    return binary_to_decimal(report.pop())


def life_support_rating(report):
    criteria = lambda ones_count, report: ones_count >= len(report) / 2
    return (
        filter_report(set(report), criteria)
        * filter_report(set(report), lambda *args: not criteria(*args))
    )


def main():
    with open("report.txt") as f:
        report = set(tuple(map(int, line.strip())) for line in f)
    print(life_support_rating(report))


if __name__ == "__main__":
    main()
