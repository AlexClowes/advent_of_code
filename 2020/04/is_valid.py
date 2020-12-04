import re


def get_passports(filename):
    with open(filename) as f:
        passport_text = f.read().split("\n\n")
    for string in passport_text:
        yield dict(kv.split(":") for kv in string.strip().replace("\n", " ").split(" "))


def is_valid(passport):
    return all(k in passport for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))


def main():
    print(sum(is_valid(p) for p in get_passports("passports.txt")))


if __name__ == "__main__":
    main()
