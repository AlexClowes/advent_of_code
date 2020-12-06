def get_responses():
    with open("responses.txt") as f:
        responses = f.read().split("\n\n")
    return (r.replace("\n", "") for r in responses)


def get_count(response):
    yes = [0] * 26
    for char in response:
        yes[ord(char) - ord("a")] = 1
    return sum(yes)


def main():
    print(sum(get_count(r) for r in get_responses()))


if __name__ == "__main__":
    main()
