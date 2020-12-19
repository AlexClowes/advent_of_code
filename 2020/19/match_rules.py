import re


def build_pattern(rules):
    pattern = rules["0"]
    while True:
        for idx, token in enumerate(pattern):
            if token.isdecimal():
                pattern = pattern[:idx] + rules[token] + pattern[idx + 1 :]
                break
        else:
            break
    return "^" + "".join(pattern) + "$"


def main():
    rules = {}
    with open("rules_messages.txt") as f:
        while (line := f.readline()) != "\n":
            rule_idx, rule = line.strip().split(": ")
            rule = rule.replace('"', "")
            if "|" in rule:
                rule = f"( {rule} )"
            rules[rule_idx] = rule.split(" ")

        messages = [line.strip() for line in f]

    pattern = build_pattern(rules)
    print(sum(bool(re.match(pattern, msg)) for msg in messages))


if __name__ == "__main__":
    main()
