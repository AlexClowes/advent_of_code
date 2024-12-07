from collections import deque
from itertools import product


def parse_brick_snapshot(snapshot):
    start, end = (
        [int(x) for x in pos.split(",")]
        for pos in snapshot.split("~")
    )
    assert sum(s != e for s, e in zip(start, end)) <= 1
    ranges = (range(x1, x2 + 1) for x1, x2 in zip(start, end))
    return set(product(*ranges))


def get_bounds(bricks):
    xmin = ymin = zmin = float("inf")
    xmax = ymax = zmax = float("-inf")
    for x, y, z in set.union(*bricks):
        xmin = min(xmin, x)
        xmax = max(xmax, x)
        ymin = min(ymin, y)
        ymax = max(ymax, y)
        zmin = min(zmin, z)
        zmax = max(zmax, z)
    return (xmin, xmax), (ymin, ymax), (zmin, zmax)


def move(points, dz):
    return {(x, y, z + dz) for x, y, z in points}


def settle(bricks):
    (xmin, xmax), (ymin, ymax), _ = get_bounds(bricks)
    stack = {
        (x, y, 0)
        for x in range(xmin, xmax + 1)
        for y in range(ymin, ymax + 1)
    }
    distance_to_fall = [-1] * len(bricks)
    distance = 0
    while any(dist == -1 for dist in distance_to_fall):
        # Add adjacent bricks to stack
        new_brick_added = True
        while new_brick_added:
            up_one = move(stack, 1)
            new_brick_added = False
            for idx, brick in enumerate(bricks):
                if distance_to_fall[idx] == -1 and brick & up_one:
                    distance_to_fall[idx] = distance
                    stack.update(brick)
                    new_brick_added = True
        # Move stack up
        stack = move(stack, 1)
        distance += 1

    return [move(brick, -dist) for brick, dist in zip(bricks, distance_to_fall)]


def get_support_graph(bricks):
    supports = [set() for _ in range(len(bricks))]
    supported_by = [set() for _ in range(len(bricks))]
    for i, supporter in enumerate(bricks):
        for j, supported in enumerate(bricks):
            if i != j and move(supporter, 1) & supported:
                supports[i].add(j)
                supported_by[j].add(i)
    return supports, supported_by


def main():
    with open("bricks.txt") as f:
        bricks = [parse_brick_snapshot(line.strip()) for line in f]
    bricks = settle(bricks)

    supports, supported_by = get_support_graph(bricks)
    total = 0
    for i, _ in enumerate(bricks):
        q = deque(supports[i])
        gone = {i}
        while q:
            brick = q.popleft()
            if not supported_by[brick] - gone:
                gone.add(brick)
                q.extend(supports[brick])
        total += len(gone) - 1
    print(total)


if __name__ == "__main__":
    main()
