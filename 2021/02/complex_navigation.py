def main():
    with open("course.txt") as f:
        course = [line.split() for line in f]

    aim = x = y = 0
    for direction, distance in course:
        if direction == "forward":
            x += int(distance)
            y += aim * int(distance)
        elif direction == "down":
            aim += int(distance)
        elif direction == "up":
            aim -= int(distance)
    print(x * y)

if __name__ == "__main__":
    main()
