from collections import deque


def sum_bits(n):
    ret = 0
    while n > 0:
        ret += n % 2
        n //= 2
    return ret


def is_open(pos):
    x, y = pos
    n = x * x + 3 * x + 2 * x * y + y + y * y + 1352
    return sum_bits(n) % 2 == 0


def adjacent(pos):
    x, y = pos
    if x > 0:
        yield x - 1, y
    yield x + 1, y
    if y > 0:
        yield x, y - 1
    yield x, y + 1


def main():
    finish = (31, 39)
    seen = set()
    q = deque()
    q.append((0, (1, 1)))
    while q:
        n_moves, pos = q.popleft()
        if pos in seen:
            continue
        seen.add(pos)
        if pos == finish:
            print(n_moves)
            return
        for new_pos in filter(is_open, adjacent(pos)):
            q.append((n_moves + 1, new_pos))


if __name__ == "__main__":
    main()
