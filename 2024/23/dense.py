from collections import defaultdict, deque


def main():
    graph = defaultdict(set)
    with open("network.txt") as f:
        for line in f:
            node1, node2 = line.strip().split("-")
            graph[node1].add(node2)
            graph[node2].add(node1)
    for node in graph:
        graph[node].add(node)

    def canonical(_set):
        return tuple(sorted(_set))

    seen = set()
    max_len = 0
    q = deque([(graph[node], {node}) for node in graph])
    while q:
        connected, checked = q.pop()
        if len(connected) <= max_len:
            continue
        if connected == checked:
            max_len = len(connected)
            max_clique = connected
            continue
        if (canonical_state := (canonical(connected), canonical(checked))) in seen:
            continue
        seen.add(canonical_state)
        q.extend(
            (connected & graph[node], checked | {node})
            for node in connected - checked
        )

    print(",".join(sorted(max_clique)))


if __name__ == "__main__":
    main()
