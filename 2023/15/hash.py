def hash(string):
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val %= 256
    return val


def main():
    with open("init_sequence.txt") as f:
        print(sum(hash(instruction) for instruction in f.read().strip().split(",")))


if __name__ == "__main__":
    main()
