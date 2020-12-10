from functools import lru_cache


def main():
    with open("adapters.txt") as f:
        adapters = sorted(int(line.strip()) for line in f)

    n_adapters = len(adapters)
    last_adapter = adapters[-1]

    @lru_cache(maxsize=None)
    def count_the_ways(val, pos):
        if val == last_adapter:
            return 1
        total = 0
        while pos < n_adapters and adapters[pos] <= val + 3:
            total += count_the_ways(adapters[pos], pos + 1)
            pos += 1
        return total

    print(count_the_ways(0, 0))


if __name__ == "__main__":
    main()
