def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x


def main():
    with open("rules_messages.txt") as f:
        rules = {}
        while (line := f.readline()) != "\n":
            rule_idx, rule = line.strip().split(": ")
            rules[int(rule_idx)] = tuple(
                tuple(map(try_int, t.split(" ")))
                for t in rule.replace('"', "").split(" | ")
            )

        messages = [line.strip() for line in f]

    def recurse(rule, message):
        # Base case
        if not rule and not message:
            return True, None
        if (rule and not message) or (not rule and message):
            return False, None

        for option in rule:
            match = True
            pos = 0
            for element in option:
                if element == "a" or element == "b":
                    match = element == message[pos]
                    pos_inc = 1
                else:
                    match, pos_inc = recurse(rules[element], message[pos:])
                if not match:
                    break
                pos += pos_inc
            else:
                break
        return match, pos

    def match(message):
        match, length = recurse(rules[0], message)
        return match and length == len(message)

    print(sum(map(match, messages)))


if __name__ == "__main__":
    main()
