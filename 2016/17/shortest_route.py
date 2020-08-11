from collections import deque
from hashlib import md5


def main():
    passcode = "qzthpkfp"

    def open_adj(position, path):
        h = md5((passcode + path).encode("utf8")).hexdigest()
        x, y = position
        if h[0] in "bcdef" and y > 1:
            yield path + "U", (x, y - 1)
        if h[1] in "bcdef" and y < 4:
            yield path + "D", (x, y + 1)
        if h[2] in "bcdef" and x > 1:
            yield path + "L", (x - 1, y)
        if h[3] in "bcdef" and x < 4:
            yield path + "R", (x + 1, y)

    q = deque()
    q.append(((1, 1), ""))
    while q:
        position, path = q.popleft()
        if position == (4, 4):
            print(path)
            return
        for new_path, new_pos in open_adj(position, path):
            q.append((new_pos, new_path))


if __name__ == "__main__":
    main()
