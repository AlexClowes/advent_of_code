from functools import lru_cache


@lru_cache(maxsize=None)
def count_the_ways(total, containers):
    if total == 0:
        return 1
    if not containers:
        return 0
    c = containers[0]
    ret = count_the_ways(total, containers[1:])
    if c <= total:
        ret += count_the_ways(total - c,  containers[1:])
    return ret


def main():
    with open("containers.txt") as f:
        containers = tuple(sorted(int(line.strip()) for line in f))
    print(count_the_ways(150, containers))


if __name__ == "__main__":
    main()
