import operator


def search_and_eval(expr, operator, action):
    # Look for appearance of operator, not contained by brackets.
    # Then evaluate that operator.
    depth = 0
    for pos, char in enumerate(expr):
        if depth == 0 and char == operator:
            left_operand = new_eval(expr[:pos])
            right_operand = new_eval(expr[pos + 1 :])
            return action(left_operand, right_operand)
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1


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

    # May need to strip leading or trailing brackets
    expr = strip_redundant_brackets(expr)

    # expr may be a single number
    if expr.isdecimal():
        return int(expr)

    return search_and_eval(expr, "*", operator.mul) or search_and_eval(expr, "+", operator.add)


def main():
    with open("homework.txt") as f:
        print(sum(new_eval(line.strip()) for line in f))


if __name__ == "__main__":
    main()
