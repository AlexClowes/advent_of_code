from collections import Counter


def decode(messages):
    counts = [Counter(m[i] for m in messages) for i in range(len(messages[0]))]
    return "".join(c.most_common(1)[0][0] for c in counts)


def main():
    with open("messages.txt") as f:
        messages = [line.strip() for line in f]
    print(decode(messages))


if __name__ == "__main__":
    main()
