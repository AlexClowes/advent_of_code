def main():
    with open("brackets.txt") as f:
        brackets = f.readline()

    floor = 0
    for idx, char in enumerate(brackets, 1):
        floor += 1 if char == "(" else -1
        if floor == -1:
            print(idx)
            break


if __name__ == "__main__":
    main()
