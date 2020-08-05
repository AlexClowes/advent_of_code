from collections import Counter
import re


def get_checksum(room_name):
    char_counts = Counter(room_name.replace("-", ""))
    return "".join(sorted(char_counts, key=lambda c: (-char_counts[c], c))[:5])


def main():
    pat = r"((?:\w+-)+)(\d+)\[(\w+)\]"
    with open("rooms.txt") as f:
        rooms = [line.strip() for line in f]
    total = 0
    for room in rooms:
        room_name, room_id, checksum = re.match(pat, room).groups()
        if get_checksum(room_name) == checksum:
            total += int(room_id)
    print(total)


if __name__ == "__main__":
    main()
