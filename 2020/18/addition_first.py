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


def search_and_eval(expr, operator):
    # Look for appearance of operator, not contained by brackets.
    # Then evaluate that operator.
    for pos, (char, depth) in enumerate(with_depth(expr)):
        if depth == 0 and char == operator:
            left_operand = new_eval(expr[:pos])
            right_operand = new_eval(expr[pos + 1 :])
            return OPERATORS[operator](left_operand, right_operand)


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

    return search_and_eval(expr, "*") or search_and_eval(expr, "+")


def main():
    with open("homework.txt") as f:
        print(sum(new_eval(line.strip()) for line in f))


if __name__ == "__main__":
    main()
