def shared_item(rucksack):
    first, second = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
    return (set(first) & set(second)).pop()


def priority(item):
    if item.isupper():
        return ord(item) - ord("A") + 27
    return ord(item) - ord("a") + 1


def main():
    with open("rucksacks.txt") as f:
        print(sum(priority(shared_item(line.strip())) for line in f))


if __name__ == "__main__":
    main()
