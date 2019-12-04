def fuel_cost(mass):
    total = 0
    while True:
        mass = mass // 3 - 2
        if mass < 0:
            break
        total += mass
    return total


def main():
    with open("masses.txt") as f:
        print(sum(fuel_cost(int(line)) for line in f))


if __name__ == "__main__":
    main()
