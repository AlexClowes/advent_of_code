from itertools import islice
import operator


OPERATORS = {"+": operator.add, "*": operator.mul}


def with_depth(expr):
    depth = 0
    for char in expr:
        yield char, depth
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1


def strip_redundant_brackets(expr):
    # Need to check that leading and trailing brackets actually match
    # e.g. (1 * 2) + (3 * 4) should not be modified
    #      (1 + 2 * 3) should be modified
    while (
        expr[0] == "("
        and expr[-1] == ")"
        and all(depth for _, depth in islice(with_depth(expr), 1, None))
    ):
        expr = expr[1:-1]
    return expr


def new_eval(expr):
    # Get rid of any whitespace
    expr = expr.replace(" ", "")

    # May need to strip leading or trailing brackets
    expr = strip_redundant_brackets(expr)

    # expr may be a single number
    if expr.isdecimal():
        return int(expr)

    # Get the right-most operator not contained by brackets.
    for pos, (char, depth) in reversed(list(enumerate(with_depth(expr)))):
        if depth == 0 and char in OPERATORS:
            break
    # Evaluate
    left_operand = new_eval(expr[:pos])
    operator = OPERATORS[char]
    right_operand = new_eval(expr[pos + 1 :])
    return operator(left_operand, right_operand)


def main():
    with open("homework.txt") as f:
        print(sum(new_eval(line.strip()) for line in f))


if __name__ == "__main__":
    main()
