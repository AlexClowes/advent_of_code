def main():
    with open("freq_changes.txt") as f:
        print(sum(int(line) for line in f))


if __name__ == "__main__":
    main()
