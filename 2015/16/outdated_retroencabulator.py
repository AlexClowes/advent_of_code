import re


items = [
    "children",
    "cats",
    "samoyeds",
    "pomeranians",
    "akitas",
    "vizslas",
    "goldfish",
    "trees",
    "cars",
    "perfumes",
]
target = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def main():
    with open("aunts.txt") as f:
        for idx, line in enumerate(f, 1):
            for item in items:
                match = re.search(rf"{item}: (\d+)", line)
                if match:
                    count = int(match.groups()[0])
                    if item in ("cats", "trees"):
                        if count <= target[item]:
                            break
                    elif item in ("pomeranians", "goldfish"):
                        if count >= target[item]:
                            break
                    elif count != target[item]:
                        break
            else:
                print(idx)


if __name__ == "__main__":
    main()
