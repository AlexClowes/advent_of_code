from collections import deque


def build_bridges(components):
    q = deque()
    q.append(((), 0, 0))
    while q:
        used_components, strength, next_port = q.popleft()
        yield len(used_components), strength
        for i, new_component in enumerate(components):
            if i not in used_components:
                if next_port in new_component:
                    if new_component[0] == next_port:
                        new_port = new_component[1]
                    else:
                        new_port = new_component[0]
                    q.append(
                        (
                            used_components + (i,),
                            strength + sum(new_component),
                            new_port,
                        )
                    )


def main():
    with open("components.txt") as f:
        components = tuple(tuple(map(int, line.strip().split("/"))) for line in f)
    bridges = list(build_bridges(components))
    print(max(strength for _, strength in bridges))
    print(max(bridges)[1])


if __name__ == "__main__":
    main()
