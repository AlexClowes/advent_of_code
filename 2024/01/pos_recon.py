def main():
    list1, list2 = [], []
    with open("lists.txt") as f:
        for line in f:
            num1, num2 = map(int, line.strip().split("   "))
            list1.append(num1)
            list2.append(num2)

    print(sum(abs(n1 - n2) for n1, n2 in zip(sorted(list1), sorted(list2))))


if __name__ == "__main__":
    main()
