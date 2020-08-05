import hashlib
from itertools import count, islice


def gen_hashes(door_id):
    for index in count():
        m = hashlib.md5()
        m.update((door_id + str(index)).encode("utf8"))
        yield m.hexdigest()


def main():
    door_id = "abbhdwsy"
    hashes = gen_hashes(door_id)
    password_chars = (h[5:7] for h in hashes if h.startswith("00000"))
    password = [""] * 8
    char_count = 0
    for pos, char in password_chars:
        if pos.isnumeric():
            pos = int(pos)
        else:
            continue
        if pos <= 7 and not password[pos]:
            password[int(pos)] = char
            char_count += 1
            if char_count == 8:
                break
    print("".join(password))


if __name__ == "__main__":
    main()
