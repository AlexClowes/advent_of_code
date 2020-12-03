def main():
    seen = set()
    with open("expenses.txt") as f:
        vals = (int(line.strip()) for line in f)
        for v in vals:
            if 2020 - v in seen:
                print(v * (2020 - v))
                return
            seen.add(v)


if __name__ == "__main__":
    main()
