def main():
    with open("course.txt") as f:
        course = [line.split() for line in f]

    x = y = 0
    for direction, distance in course:
        if direction == "forward":
            x += int(distance)
        elif direction == "down":
            y += int(distance)
        elif direction == "up":
            y -= int(distance)
    print(x * y)

if __name__ == "__main__":
    main()
