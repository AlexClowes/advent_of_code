WORD2DIGIT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def get_digits(line):
    pos = 0
    while pos < len(line):
        if line[pos].isdigit():
            yield int(line[pos])
            pos += 1
        else:
            for word, digit in WORD2DIGIT.items():
                if line[pos : pos + len(word)] == word:
                    yield digit
                    pos += len(word)
                    break
            else:
                pos += 1

def main():
    with open("calibration_doc.txt") as f:
        total = 0
        for line in f:
            digits = list(get_digits(line))
            total += 10 * digits[0] + digits[-1]
        print(total)




if __name__ == "__main__":
    main()
