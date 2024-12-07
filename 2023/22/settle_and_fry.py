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


def can_zap(bricks):
    supported_by = [[] for _ in range(len(bricks))]
    for i, brick in enumerate(bricks):
        for j, other in enumerate(bricks):
            if i != j and move(brick, -1) & other:
                supported_by[i].append(j)
    ret = [True] * len(bricks)
    for supporters in supported_by:
        if len(supporters) == 1:
            ret[supporters[0]] = False
    return ret


def main():
    with open("bricks.txt") as f:
        bricks = [parse_brick_snapshot(line.strip()) for line in f]
    bricks = settle(bricks)
    print(sum(can_zap(bricks)))


if __name__ == "__main__":
    main()
