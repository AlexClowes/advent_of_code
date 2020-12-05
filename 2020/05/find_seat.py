def seat_id(seat):
    return int(
        seat.translate(str.maketrans({"F": "0", "B": "1", "L": "0", "R": "1"})), 2
    )


def main():
    free_seats = set(range(1024))
    with open("seats.txt") as f:
        for line in f:
            free_seats.remove(seat_id(line.strip()))

    for seat in free_seats:
        if seat - 1 not in free_seats and seat + 1 not in free_seats:
            print(seat)


if __name__ == "__main__":
    main()
