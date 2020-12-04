import re


def get_passports(filename):
    with open(filename) as f:
        passport_text = f.read().split("\n\n")
    for string in passport_text:
        yield dict(kv.split(":") for kv in string.strip().replace("\n", " ").split(" "))


def is_valid(passport):
    tests = {
        "byr": lambda x: re.match(r"^[0-9]{4}$", x) and 1920 <= int(x) <= 2002,
        "iyr": lambda x: re.match(r"^[0-9]{4}$", x) and 2010 <= int(x) <= 2020,
        "eyr": lambda x: re.match(r"^[0-9]{4}$", x) and 2020 <= int(x) <= 2030,
        "hgt": lambda x: (
            (re.match(r"^[0-9]{3}cm$", x) and 150 <= int(x[:-2]) <= 193)
            or (re.match(r"^[0-9]{2}in$", x) and 59 <= int(x[:-2]) <= 76)
        ),
        "hcl": lambda x: re.match(r"^#[0-9a-f]{6}", x),
        "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid": lambda x: re.match(r"^[0-9]{9}$", x),
    }

    return all(key in passport and test(passport[key]) for key, test in tests.items())


def main():
    print(sum(is_valid(p) for p in get_passports("passports.txt")))


if __name__ == "__main__":
    main()
