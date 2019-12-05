def main():
    with open("spreadsheet.txt") as f:
        rows = ([int(n) for n in line.split()] for line in f)
        print(sum(max(row) - min(row) for row in rows))


if __name__ == "__main__":
    main()
