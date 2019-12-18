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
    return keys[1:]


def main():
    with open("tunnels.txt") as f:
        tunnel_map = [line.strip() for line in f]
    tunnel_map = np.array([list(line) for line in tunnel_map])

    key_map = {}
    for i in range(tunnel_map.shape[0]):
        for j in range(tunnel_map.shape[1]):
            if tunnel_map[i, j].islower() or tunnel_map[i, j] == "@":
                key_map[tunnel_map[i, j]] = get_key_dist_req(tunnel_map, (i, j))

    memo = {}
    def shortest_path(collected_keys, current_key, path_len):
        memo_args = tuple(sorted(collected_keys)), current_key
        if memo_args not in memo or memo[memo_args][0] > path_len:
            if key_map.keys() == collected_keys:
                memo[memo_args] = path_len, path_len
            else:
                memo[memo_args] = path_len, min(
                    shortest_path(collected_keys | {next_key}, next_key, path_len + dist)
                    for next_key, dist, req_keys in key_map[current_key]
                    if next_key not in collected_keys and not req_keys - collected_keys
                )
        return memo[memo_args][1]
        
    print(shortest_path({"@"}, "@", 0))


if __name__ == "__main__":
    main()
