def main():
    with open("trees.txt") as f:
        trees = [line.strip() for line in f]
    height = len(trees)
    width = len(trees[0])

    def count_slope(right, down):
        x, y = 0, 0
        count = 0
        while y < height:
            count += trees[y][x] == "#"
            y += down
            x = (x + right) % width
        return count

    print(count_slope(3, 1))

    prod = 1
    for r, d in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        prod *= count_slope(r, d)
    print(prod)


if __name__ == "__main__":
    main()
