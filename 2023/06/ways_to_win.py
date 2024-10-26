from math import ceil, floor, prod, sqrt

def ways_to_win(time, distance):
    distance += 0.001
    return (
        floor(time / 2 + sqrt(time * time / 4 - distance))
        - ceil(time / 2 - sqrt(time * time / 4 - distance))
         + 1
    )


def main():
    with open("records.txt") as f:
        times = [int(t) for t in f.readline().strip().split()[1:]]
        distances = [int(t) for t in f.readline().strip().split()[1:]]

    print(prod(ways_to_win(time, distance) for time, distance in zip(times, distances)))



if __name__ == "__main__":
    main()
