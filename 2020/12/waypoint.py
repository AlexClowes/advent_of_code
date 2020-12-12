def main():
    with open("directions.txt") as f:
        directions = [(line[0], int(line.strip()[1:])) for line in f]

    waypoint = complex(10, 1)
    position = complex(0)

    displacement = {
        "N": complex(0, 1),
        "S": complex(0, -1),
        "E": complex(1, 0),
        "W": complex(-1, 0),
    }
    for op, operand in directions:
        if op in "NSEW":
            waypoint += operand * displacement[op]
        elif op == "L":
            waypoint *= complex(0, 1) ** (operand // 90)
        elif op == "R":
            waypoint *= complex(0, -1) ** (operand // 90)
        elif op == "F":
            position += operand * waypoint
        else:
            raise ValueError(f"Unrecognised op {op}")
    print(abs(position.real) + abs(position.imag))


if __name__ == "__main__":
    main()
