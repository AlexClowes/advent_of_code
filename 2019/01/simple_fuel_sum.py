def main():
    with open("masses.txt") as f:
        print(sum(int(l) // 3 - 2 for l in f))


if __name__ == "__main__":
    main()
