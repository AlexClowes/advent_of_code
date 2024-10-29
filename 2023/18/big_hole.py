import re


HEADINGS = {"0": (0, 1), "1": (1, 0), "2": (0, -1), "3": (-1, 0)}


def parse_line(line):
    hexcode, heading_str = re.match("\w \d+ \(#([\d\w]{5})(\d)\)", line).groups()
    return HEADINGS[heading_str], int(hexcode, 16)


def main():
    # Dig trench
    with open("dig_plan.txt") as f:
        area = 0
        boundary_points = 0
        i = j = 0
        for line in f:
            (di, dj), dist = parse_line(line.strip())

            boundary_points += dist

            new_i, new_j = i + di * dist, j + dj * dist
            area += (i * new_j - j * new_i) / 2
            i, j = new_i, new_j

    print(int(abs(area) + boundary_points / 2 + 1))


if __name__ == "__main__":
    main()
