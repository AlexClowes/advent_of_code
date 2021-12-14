from collections import defaultdict, deque


def main():
    graph = defaultdict(set)
    with open("map.txt") as f:
        for line in f:
            start, end = line.strip().split("-")
            graph[start].add(end)
            graph[end].add(start)

    path_count = 0
    q = deque((("start", set(), False),))
    while q:
        current, seen, double = q.popleft()
        for node in graph[current]:
            if node == "start":
                continue
            elif node == "end":
                path_count += 1
            elif node.isupper():
                q.append((node, seen, double))
            elif node not in seen:
                q.append((node, set(seen) | {node}, double))
            elif not double:
                q.append((node, seen, True))
    print(path_count)


if __name__ == "__main__":
    main()
