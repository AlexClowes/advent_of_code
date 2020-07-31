from functools import lru_cache
import operator


unary_operations = {
    "NOT": operator.inv,
}
binary_operations = {
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
}


def tokenise(value):
    tokens = [int(t) if t.isdigit() else t for t in value.split()]
    if len(tokens) == 1:
        return tokens[0]
    elif len(tokens) == 2:
        return unary_operations[tokens[0]], tokens[1]
    elif len(tokens) == 3:
        return binary_operations[tokens[1]], tokens[0], tokens[2]
    else:
        raise ValueError(f"Cannot parse instruction {value}")


def main():
    instructions = {}
    with open("instructions.txt") as f:
        for line in f.readlines():
            value, name = line.strip().split(" -> ")
            instructions[name] = tokenise(value)

    @lru_cache(maxsize=None)
    def evaluate(name):
        value = instructions[name]
        if isinstance(value, int):
            return value
        elif isinstance(value, str):
            return evaluate(value)
        else:
            op, *args = value
            args = (evaluate(a) if not isinstance(a, int) else a for a in args)
            return op(*args)

    a_val = evaluate("a")
    evaluate.cache_clear()
    instructions["b"] = a_val
    print(evaluate("a"))


if __name__ == "__main__":
    main()
