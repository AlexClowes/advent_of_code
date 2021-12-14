from collections import defaultdict, deque


def main():
    graph = defaultdict(set)
    with open("map.txt") as f:
        for line in f:
            start, end = line.strip().split("-")
            graph[start].add(end)
            graph[end].add(start)

    path_count = 0
    q = deque((("start", {"start"}),))
    while q:
        current, seen = q.popleft()
        for node in graph[current]:
            if node == "end":
                path_count += 1
            elif node.isupper():
                q.append((node, seen))
            elif node not in seen:
                q.append((node, set(seen) | {node}))
    print(path_count)


if __name__ == "__main__":
    main()
