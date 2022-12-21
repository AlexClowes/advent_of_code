import operator


OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}


# Solutions for "a op b = c" where c and one of a, b are known
SOLVE = {
    "+": lambda a, b, c: c - b if b else c - a,
    "-": lambda a, b, c: b + c if b else a - c,
    "*": lambda a, b, c: c // b if b else c // a,
    "/": lambda a, b, c: b * c if b else a // c,
}


def main():
    with open("jobs.txt") as f:
        jobs = dict(line.strip().split(": ") for line in f)

    l1, _, l2 = jobs["root"].split()
    jobs["root"] = l1 + " - " + l2
    jobs["humn"] = ""

    def evaluate(label):
        try:
            match jobs[label].split():
                case n,:
                    return int(n)
                case label1, op, label2:
                    return OPS[op](evaluate(label1), evaluate(label2))
        except TypeError:
            pass

    def set_to_val(label, val):
        match jobs[label].split():
            case n,:
                if int(n) != val:
                    raise ValueError("Contradiction")
            case label1, op, label2:
                v1, v2 = evaluate(label1), evaluate(label2)
                if not (v1 or v2):
                    raise ValueError("Two unknowns")
                if v1 and v2:
                    assert OPS[op](v1, v2) == val
                set_to_val(label2 if v1 else label1, SOLVE[op](v1, v2, val))
        jobs[label] = val

    set_to_val("root", 0)
    print(jobs["humn"])


if __name__ == "__main__":
    main()
