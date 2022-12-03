def shared_item(first, second, third):
    return (set(first) & set(second) & set(third)).pop()


def priority(item):
    if item.isupper():
        return ord(item) - ord("A") + 27
    return ord(item) - ord("a") + 1

def grouper(n, iterable):
    return zip(*(iter(iterable) for _ in range(n)))


def main():
    with open("rucksacks.txt") as f:
        groups = grouper(3, (line.strip() for line in f))
        print(sum(priority(shared_item(*group)) for group in groups))


if __name__ == "__main__":
    main()
