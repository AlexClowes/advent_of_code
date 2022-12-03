def main():
    with open("elf_rations.txt") as f:
        elves = f.read().strip().split("\n\n")
        calories = (sum(map(int, elf.split("\n"))) for elf in elves)
        print(max(calories))


if __name__ == "__main__":
    main()
