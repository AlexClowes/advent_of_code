def main():
    with open("directions.txt") as f:
        directions = f.readline()

    visited_houses = {(0, 0)}
    x, y = 0, 0
    for d in directions[::2]:
        if d == "^":
            y += 1
        elif d == "v":
            y -= 1
        elif d == ">":
            x += 1
        elif d == "<":
            x -= 1
        visited_houses.add((x, y))
    x, y = 0, 0
    for d in directions[1::2]:
        if d == "^":
            y += 1
        elif d == "v":
            y -= 1
        elif d == ">":
            x += 1
        elif d == "<":
            x -= 1
        visited_houses.add((x, y))
    print(len(visited_houses))


if __name__ == "__main__":
    main()
