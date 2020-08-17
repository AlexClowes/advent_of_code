from collections import defaultdict, deque


def main():
    pipes = defaultdict(set)
    with open("pipes.txt") as f:
        for line in f:
            start, ends = line.strip().split(" <-> ")
            pipes[int(start)].update(map(int, ends.split(", ")))

    def get_group(node):
        group = set()
        q = deque((node,))
        while q:
            node = q.popleft()
            group.add(node)
            for new_node in pipes[node]:
                if new_node not in group:
                    q.append(new_node)
        return group

    print(len(get_group(0)))

    n_groups = 0
    seen = set()
    for node in pipes:
        if node not in seen:
            n_groups += 1
            seen.update(get_group(node))
    print(n_groups)


if __name__ == "__main__":
    main()
