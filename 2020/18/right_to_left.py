import operator


OPERATORS = {"+": operator.add, "*": operator.mul}


def strip_redundant_brackets(expr):
    # Need to check that leading and trailing brackets actually match
    # e.g. (1 * 2) + (3 * 4) should not be modified
    #      (1 + 2 * 3) should be modified
    done = False
    while expr.startswith("(") and expr.endswith(")") and not done:
        done = True
        depth = 1
        for char in expr[1:]:
            if depth == 0:
                break
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
        else:
            expr = expr[1:-1]
            done = False
    return expr


def new_eval(expr):
    # Get rid of any whitespace
    expr = expr.replace(" ", "")

    # expr may be a single number
    if expr.isdecimal():
        return int(expr)

    # May need to strip leading or trailing brackets
    expr = strip_redundant_brackets(expr)

    # We need to get the operator, and left and right operands.
    depth = 0
    for pos, char in reversed(list(enumerate(expr))):
        if depth == 0 and char in OPERATORS:
            break
        elif char == ")":
            depth += 1
        elif char == "(":
            depth -= 1
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
