def main():
    with open("ingredients.txt") as f:
        fresh_ranges = []
        for line in f:
            if not line.strip():
                break
            start, end = map(int, line.split("-"))
            fresh_ranges.append(range(start, end + 1))

        def is_fresh(ingredient):
            return any(ingredient in fresh_range for fresh_range in fresh_ranges)

        print(sum(is_fresh(int(line.strip())) for line in f))


if __name__ == "__main__":
    main()
