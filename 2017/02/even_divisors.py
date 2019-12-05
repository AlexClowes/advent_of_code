def result(row):
    for i in range(len(row) - 1):
        for j in range(i + 1, len(row)):
            if row[i] % row[j] == 0:
                return row[i] // row[j]
            elif row[j] % row[i] == 0:
                return row[j] // row[i]


def main():
    with open("spreadsheet.txt") as f:
        rows = ([int(n) for n in line.split()] for line in f)
        print(sum(result(row) for row in rows))


if __name__ == "__main__":
    main()
