def distance(str1, str2):
    return sum(char1 != char2 for char1, char2 in zip(str1, str2))


def common_letters(box_ids):
    for id1 in box_ids:
        for id2 in box_ids:
            if distance(id1, id2) == 1:
                return "".join(char1 for char1, char2 in zip(id1, id2) if char1 == char2)

def main():
    with open("box_ids.txt") as f:
        box_ids = [line.strip() for line in f]
        print(common_letters(box_ids))


if __name__ == "__main__":
    main()
