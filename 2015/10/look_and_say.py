from itertools import groupby


def look_and_say(n):
    return "".join(str(len(list(group))) + digit for digit, group in groupby(n))


def main():
    n = "3113322113"
    for _ in range(40):
        n = look_and_say(n)
    print(len(n))
    for _ in range(10):
        n = look_and_say(n)
    print(len(n))


if __name__ == "__main__":
    main()
