from collections import deque


def dist(point1, point2):
    return sum(abs(x - y) for x, y in zip(point1, point2))


def contains(constellation, point):
    return any(dist(point, other) <= 3 for other in constellation)


def main():
    # Build graph with points as vertices, with an edge if two points have distance
    # <= 3 between them
    graph = {}
    with open("points.txt") as f:
        for line in f:
            point = tuple(map(int, line.strip().split(",")))
            graph[point] = set()
            for other_point in graph:
                if dist(other_point, point) <= 3:
                    graph[point].add(other_point)
                    graph[other_point].add(point)

    # Get constellations
    seen = set()
    constellations = 0
    for point in graph:
        if point not in seen:
            q = deque((point,))
            constellations += 1
            while q:
                current_point = q.popleft()
                if current_point not in seen:
                    seen.add(current_point)
                    q.extend(graph[current_point])
    print(constellations)


if __name__ == "__main__":
    main()
