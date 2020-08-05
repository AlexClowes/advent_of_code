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
    password_chars = (h[5] for h in hashes if h.startswith("00000"))
    print("".join(islice(password_chars, 8)))


if __name__ == "__main__":
    main()
