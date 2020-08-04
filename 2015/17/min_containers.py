def count_minimal_ways(total, containers):
    min_ways = float("inf")

    def gen_ways(total, free_containers, used_containers):
        nonlocal min_ways
        if used_containers == min_ways and total > 0:
            return
        if total == 0:
            yield used_containers
            return
        if not free_containers:
            return
        yield from gen_ways(total, free_containers[1:], used_containers)
        c = free_containers[0]
        if c <= total:
            yield from gen_ways(total - c, free_containers[1:], used_containers + 1)

    for used_containers in gen_ways(total, containers, 0):
        if used_containers < min_ways:
            min_ways = used_containers
            min_count = 1
        elif used_containers == min_ways:
            min_count += 1
    return min_count


def main():
    with open("containers.txt") as f:
        containers = tuple(int(line.strip()) for line in f)
    print(count_minimal_ways(150, containers))


if __name__ == "__main__":
    main()
