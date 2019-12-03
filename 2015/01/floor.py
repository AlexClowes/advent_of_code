def main():
    with open("brackets.txt") as f:
        brackets = f.readline()
    print(brackets.count("(") - brackets.count(")"))


if __name__ == "__main__":
    main()
