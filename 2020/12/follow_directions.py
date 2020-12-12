def main():
    with open("directions.txt") as f:
        directions = [(line[0], int(line.strip()[1:])) for line in f]

    heading = complex(1)
    position = complex(0)

    displacement = {
        "N": complex(0, 1),
        "S": complex(0, -1),
        "E": complex(1, 0),
        "W": complex(-1, 0),
    }
    for op, operand in directions:
        if op in "NSEW":
            position += operand * displacement[op]
        elif op == "L":
            heading *= complex(0, 1) ** (operand // 90)
        elif op == "R":
            heading *= complex(0, -1) ** (operand // 90)
        elif op == "F":
            position += operand * heading
        else:
            raise ValueError(f"Unrecognised op {op}")
    print(abs(position.real) + abs(position.imag))


if __name__ == "__main__":
    main()
