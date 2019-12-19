from collections import deque

import numpy as np


def adjacent(i, j):
    yield i + 1, j
    yield i - 1, j
    yield i, j + 1
    yield i, j - 1


def get_key_dist_req(tunnel_map, start_pos):
    """
    Return list of (key, distance, required_keys) tuples, starting from start_pos.
    """
    keys = []
    seen = {start_pos}
    q = deque()
    q.append((start_pos, 0, set()))
    while q:
        pos, dist, req_keys = q.popleft()
        char = tunnel_map[pos]
        if char.islower():
            keys.append((char, dist, req_keys))
        for adj in adjacent(*pos):
            if adj not in seen and tunnel_map[adj] != "#":
                seen.add(adj)
                if tunnel_map[adj].isupper():
                    q.append((adj, dist + 1, req_keys | {tunnel_map[adj].lower()}))
                else:
                    q.append((adj, dist + 1, req_keys))
    return keys


def split(tunnel_map):
    size = tunnel_map.shape
    center = (
        slice(size[0] // 2 - 1, size[0] // 2 + 2),
        slice(size[1] // 2 - 1, size[1] // 2 + 2),
    )
    replacement = np.array([
        ["1", "#", "2"],
        ["#", "#", "#"],
        ["3", "#", "4"],
    ])
    tunnel_map[center] = replacement


def main():
    with open("tunnels.txt") as f:
        tunnel_map = [line.strip() for line in f]
    tunnel_map = np.array([list(line) for line in tunnel_map])
    split(tunnel_map)

    key_map = {}
    for i in range(tunnel_map.shape[0]):
        for j in range(tunnel_map.shape[1]):
            if tunnel_map[i, j].islower() or tunnel_map[i, j] in "1234":
                key_map[tunnel_map[i, j]] = get_key_dist_req(tunnel_map, (i, j))

    memo = {}
    def shortest_path(collected_keys, current_keys, path_len):
        memo_args = tuple(sorted(collected_keys)), tuple(current_keys)
        if memo_args not in memo or memo[memo_args][0] > path_len:
            if key_map.keys() == collected_keys:
                memo[memo_args] = path_len, path_len
            else:
                min_path_len = 99999999
                for i, key in enumerate(current_keys):
                    for next_key, dist, req_keys in key_map[key]:
                        if next_key in collected_keys or req_keys - collected_keys:
                            continue
                        new_state = list(current_keys)
                        new_state[i] = next_key
                        min_path_len = min(
                            shortest_path(
                                collected_keys | {next_key}, new_state, path_len + dist
                            ),
                            min_path_len,
                        )
                memo[memo_args] = path_len, min_path_len
        return memo[memo_args][1]

    print(shortest_path({"1", "2", "3", "4"}, ["1", "2", "3", "4"], 0))


if __name__ == "__main__":
    main()
