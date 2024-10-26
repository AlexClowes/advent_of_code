from math import ceil, floor, sqrt

def ways_to_win(time, distance):
    distance += 0.001
    return (
        floor(time / 2 + sqrt(time * time / 4 - distance))
        - ceil(time / 2 - sqrt(time * time / 4 - distance))
         + 1
    )


def main():
    with open("records.txt") as f:
        time = int("".join(f.readline().strip().split()[1:]))
        distance = int("".join(f.readline().strip().split()[1:]))

    print(ways_to_win(time, distance))


if __name__ == "__main__":
    main()
