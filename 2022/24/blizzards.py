from collections import defaultdict, deque
import numpy as np


def main():
    with open("map.txt") as f:
        data = np.array([list(line.strip()) for line in f])[1:-1, 1:-1]
        
    height, width = data.shape

    horizontal_block = np.zeros(data.shape + (width,), dtype=bool)
    vertical_block = np.zeros(data.shape + (height,), dtype=bool)

    for (i, j), char in np.ndenumerate(data):
        if char in "<>":
            sign = 1 if char == ">" else -1
            for t in range(width):
                horizontal_block[i, (j + sign * t) % width, t] = True
        elif char in "^v":
            sign = 1 if char == "v" else -1
            for t in range(height):
                vertical_block[(i + sign * t) % height, j, t] = True

    START = (-1, 0)
    END = (height, width - 1)

    adj = defaultdict(set)
    adj[START].update((START, (START[0] + 1, START[1])))
    adj[END].update((END, (END[0] - 1, END[1])))
    adj[START[0] + 1, START[1]].add(START)
    adj[END[0] - 1, END[1]].add(END)
    for (i, j), _ in np.ndenumerate(data):
        adj[i, j].add((i, j))
        if i > 0:
            adj[i, j].add((i - 1, j))
        if i < height - 1:
            adj[i, j].add((i + 1, j))
        if j > 0:
            adj[i, j].add((i, j - 1))
        if j < width - 1:
            adj[i, j].add((i, j + 1))

    def get_min_time(start_pos, end_pos, start_time):
        q = deque([(start_pos, start_time)])
        seen = set()
        while q:
            pos, t = q.popleft()
            if pos == end_pos:
                return t
            if (pos, t) in seen:
                continue
            seen.add((pos, t))
            new_t = t + 1
            for new_pos in adj[pos]:
                if (
                    new_pos in (START, END)
                    or (
                        not horizontal_block[*new_pos, new_t % width]
                        and not vertical_block[*new_pos, new_t % height]
                    )
                ):
                    q.append((new_pos, new_t))

    first_leg = get_min_time(START, END, 0)
    print(first_leg)
    second_leg = get_min_time(END, START, first_leg)
    third_leg = get_min_time(START, END, second_leg)
    print(third_leg)


if __name__ == "__main__":
    main()
