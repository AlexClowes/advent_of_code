import operator


OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}


def main():
    with open("jobs.txt") as f:
        jobs = dict(line.strip().split(": ") for line in f)

    def evaluate(label):
        match jobs[label].split():
            case n,:
                return int(n)
            case label1, op, label2:
                return OPS[op](evaluate(label1), evaluate(label2))

    print(evaluate("root"))


if __name__ == "__main__":
    main()
