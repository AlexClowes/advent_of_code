from collections import Counter, namedtuple
import re


Node = namedtuple("Node", "name weight children")


def main():
    with open("towers.txt") as f:
        lines = [line.strip() for line in f]

    nodes = {}
    for line in lines:
        name, weight = re.match(r"(\w+) \((\d+)\)", line).groups()
        nodes[name] = Node(name, int(weight), [])
    child_nodes = set()
    for line, parent in zip(lines, nodes.values()):
        s = line.split(" -> ")
        if len(s) == 2:
            for name in s[1].split(", "):
                parent.children.append(nodes[name])
                child_nodes.add(name)

    root = nodes[(nodes.keys() - child_nodes).pop()]
    print(root.name)

    cache = {}
    def total_weight(node):
        if node.name not in cache:
            cache[node.name] = node.weight + sum(map(total_weight, node.children))
        return cache[node.name]

    current_node = root
    while True:
        weights = [total_weight(child) for child in current_node.children]
        weight_count = Counter(weights).most_common()
        if len(weight_count) == 1:
            # current_node is the unbalanced one
            fix = target_weight - (total_weight(current_node) - current_node.weight)
            break
        else:
            target_weight = weight_count[0][0]
            bad_weight = weight_count[1][0]
            current_node = current_node.children[weights.index(bad_weight)]

    print(fix)


if __name__ == "__main__":
    main()
