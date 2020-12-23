def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x


def main():
    # Rules are represented as a tuple where each element is an option.
    # Options are represented as tuples, where each element is an int
    # (corresponding to a rule) or a character (always "a" or "b" in this case).
    with open("rules_messages.txt") as f:
        rules = {}
        while (line := f.readline()) != "\n":
            rule_idx, rule = line.strip().split(": ")
            rules[int(rule_idx)] = tuple(
                tuple(map(try_int, t.split(" ")))
                for t in rule.replace('"', "").split(" | ")
            )

        messages = [line.strip() for line in f]

    def match_option(option, message):
        """Yield all pos s.t. option matches message[:pos]"""
        if option:
            if not message:
                return
            rule = option[0]
            if isinstance(rule, str):
                if rule == message[0]:
                    yield 1
            elif isinstance(rule, int):
                for pos in match_rule(rules[rule], message):
                    for pos_inc in match_option(option[1:], message[pos:]):
                        yield pos + pos_inc
            else:
                raise ValueError(f"Unable to interpret rule {rule} in option {option}")
        else:
            yield 0

    def match_rule(rule, message):
        """Yield all pos s.t. rule matches message[:pos]"""
        for option in rule:
            yield from match_option(option, message)

    def match(message):
        return any(length == len(message) for length in match_rule(rules[0], message))

    # Part 1
    print(sum(map(match, messages)))

    # Part 2
    rules[8] = ((42,), (42, 8))
    rules[11] = ((42, 31), (42, 11, 31))
    print(sum(map(match, messages)))


if __name__ == "__main__":
    main()
