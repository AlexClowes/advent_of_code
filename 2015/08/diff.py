def main():
    with open("strings.txt") as f:
        lines = (l.strip() for l in f.readlines())
    print(sum(len(l) - len(eval(l)) for l in lines))


if __name__ == "__main__":
    main()
