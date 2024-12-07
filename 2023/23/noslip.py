import numpy as np


def main():
    with open("map.txt") as f:
        arr = np.array([list(line.strip()) for line in f])
    height, width = arr.shape
    start = (0, 1)
    end = (height - 1, width - 2)

    def adj(i, j):
        if i > 0:
            yield i - 1, j
        if i < height - 1:
            yield i + 1, j
        if j > 0:
            yield i, j - 1
        if j < width - 1:
            yield i, j + 1

    graph = {}
    for (i, j), char in np.ndenumerate(arr):
        if char != "#":
            graph[i, j] = {pos: 1 for pos in adj(i, j) if arr[pos] != "#"}

    while can_remove := [node for node, edges in graph.items() if len(edges) == 2]:
        for node in can_remove:
            (node1, weight1), (node2, weight2) = graph[node].items()
            del graph[node], graph[node1][node], graph[node2][node]
            graph[node1][node2] = graph[node2][node1] = weight1 + weight2

    q = [({start}, start, 0)]
    maxdist = 0
    while q:
        path, pos, dist = q.pop()
        if pos == end:
            maxdist = max(dist, maxdist)
        else:
            q.extend(
                (path | {next_step}, next_step, dist + graph[pos][next_step])
                for next_step in graph[pos].keys() - path
            )
    print(maxdist)


if __name__ == "__main__":
    main()
