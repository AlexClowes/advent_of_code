def is_valid(passphrase):
    words_seen = set()
    for word in passphrase.split():
        word = "".join(sorted(word))
        if word in words_seen:
            return False
        words_seen.add(word)
    return True


def main():
    with open("passphrases.txt") as f:
        print(sum(is_valid(line.strip()) for line in f))


if __name__ == "__main__":
    main()
