def get_responses():
    with open("responses.txt") as f:
        responses = f.read().strip().split("\n\n")
    return (r.split("\n") for r in responses)


def count_all_yes(response):
    count = [0] * 26
    for char in "".join(response):
        count[ord(char) - ord("a")] += 1
    return sum(c == len(response) for c in count)


def main():
    print(sum(count_all_yes(r) for r in get_responses()))


if __name__ == "__main__":
    main()
