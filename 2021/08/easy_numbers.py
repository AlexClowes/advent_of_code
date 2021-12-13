def main():
    unique_segments_count = 0
    with open("lights.txt") as f:
        for line in f:
            patterns, outputs = (chunk.split() for chunk in line.strip().split(" | "))
            for digit in outputs:
                if len(digit) in (2, 4, 3, 7):
                    unique_segments_count += 1
    print(unique_segments_count)


if __name__ == "__main__":
    main()
