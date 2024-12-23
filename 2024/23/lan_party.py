from collections import defaultdict
from itertools import combinations


def main():
    graph = defaultdict(set)
    with open("network.txt") as f:
        for line in f:
            node1, node2 = line.strip().split("-")
            graph[node1].add(node2)
            graph[node2].add(node1)

    triples = {
        tuple(sorted((tnode, node1, node2)))
        for tnode in graph
        for node1, node2 in combinations(graph[tnode], 2)
        if tnode.startswith("t")
        and node1 in graph[node2]
    }
    print(len(triples))


if __name__ == "__main__":
    main()
