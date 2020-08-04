def code_no(col, row):
    return (col + row - 1) * (col + row) // 2 - row + 1


def main():
    col, row = 3029, 2947
    #col, row = 1, 1
    n = code_no(col, row)
    code = 20151125
    for _ in range(n - 1):
        code = (252533 * code) % 33554393
    print(code)


if __name__ == "__main__":
    main()
