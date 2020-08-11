from collections import deque
from hashlib import md5
from itertools import count, islice


def has_triple(string):
    for c1, c2, c3 in zip(string, string[1:], string[2:]):
        if c1 == c2 == c3:
            return c1
    return False


def gen_hashes(salt):
    for index in count():
        yield md5((salt + str(index)).encode("utf8")).hexdigest()


def main():
    salt = "ihaygndm"
    hashgen = gen_hashes(salt)
    hash_queue = deque(islice(hashgen, 1000))

    key_count = 0
    for idx in count():
        candidate = hash_queue.popleft()
        hash_queue.append(next(hashgen))
        trip_char = has_triple(candidate)
        if trip_char and any(trip_char * 5 in h for h in hash_queue):
            key_count += 1
            if key_count == 64:
                print(idx)
                return


if __name__ == "__main__":
    main()
