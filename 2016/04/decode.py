import re


def shift(char, n):
    if char == "-":
        return " "
    return chr(((ord(char) - ord("a")) + n) % 26 + ord("a"))


def decode(coded_name, n):
    return "".join(shift(char, n) for char in coded_name)


def main():
    pat = r"((?:\w+-)+)(\d+)"
    with open("rooms.txt") as f:
        for room in f:
            coded_name, room_id = re.match(pat, room).groups()
            decoded_name = decode(coded_name, int(room_id))
            if "object" in decoded_name:
                print(room_id)


if __name__ == "__main__":
    main()
