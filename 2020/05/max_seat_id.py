def seat_id(seat):
    return int(
        seat.translate(str.maketrans({"F": "0", "B": "1", "L": "0", "R": "1"})), 2
    )


def main():
    with open("seats.txt") as f:
        print(max(seat_id(line.strip()) for line in f))


if __name__ == "__main__":
    main()
