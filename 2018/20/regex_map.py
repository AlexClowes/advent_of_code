from collections import defaultdict, deque


HEADINGS = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}


def get_options(path_expr):
    # Get each option from option list
    options = set()
    option_start = 1
    depth = 0
    for option_end, char in enumerate(path_expr):
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                options.add(path_expr[option_start:option_end])
                break
        elif depth == 1 and char == "|":
            options.add(path_expr[option_start:option_end])
            option_start = option_end + 1

    for option in options:
        yield option + path_expr[option_end + 1 :]


def build_graph(regex):
    graph = defaultdict(set)
    paths = {((0, 0), regex)}
    while paths:
        # Expand options
        while True:
            for pos, path_expr in tuple(paths):
                if path_expr.startswith("("):
                    paths.remove((pos, path_expr))
                    for option in get_options(path_expr):
                        paths.add((pos, option))
                    break
            else:
                break
        # Iterate
        new_paths = set()
        for (x, y), path_expr in paths:
            if path_expr:
                heading = HEADINGS[path_expr[0]]
                new_x, new_y = x + heading[0], y + heading[1]
                graph[x, y].add((new_x, new_y))
                graph[new_x, new_y].add((x, y))
                new_paths.add(((new_x, new_y), path_expr[1:]))
        paths = new_paths

    return graph


def room_distances(graph, start):
    distances = {}
    q = deque(((start, 0),))
    while q:
        pos, dist = q.popleft()
        if pos not in distances:
            distances[pos] = dist
            q.extend((adj, dist + 1) for adj in graph[pos])
    return distances


def main():
    with open("regex.txt") as f:
        regex = f.readline()[1:-2]

    graph = build_graph(regex)

    distances = room_distances(graph, (0, 0))

    print(max(distances.values()))
    print(sum(d >= 1000 for d in distances.values()))


if __name__ == "__main__":
    main()
