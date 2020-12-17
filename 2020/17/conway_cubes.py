from itertools import chain, product


def adj(point, dims):
    yield from (
        tuple(p + o for p, o in zip(point, offset))
        for offset in product((-1, 0, 1), repeat=dims)
        if any(offset)
    )


def iterate(state, dims):
    new_state = set()
    for point in set(chain.from_iterable(adj(p, dims) for p in state)):
        active_neighbours = sum(a in state for a in adj(point, dims))
        if active_neighbours == 3 or (active_neighbours == 2 and point in state):
            new_state.add(point)
    return new_state


def main():
    with open("initial_state.txt") as f:
        initial_state = set(
            chain.from_iterable(
                ((x, y) for x, char in enumerate(line.strip()) if char == "#")
                for y, line in enumerate(f)
            )
        )

    # 3d
    state = {(x, y, 0) for x, y in initial_state}
    for _ in range(6):
        state = iterate(state, 3)
    print(len(state))

    # 4d
    state = {(x, y, 0, 0) for x, y in initial_state}
    for _ in range(6):
        state = iterate(state, 4)
    print(len(state))


if __name__ == "__main__":
    main()
