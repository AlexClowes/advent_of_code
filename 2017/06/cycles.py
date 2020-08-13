from itertools import count


def balance(memory_banks):
    memory_banks = list(memory_banks)
    max_mem = 0
    for pos, mem in enumerate(memory_banks):
        if mem > max_mem:
            max_mem = mem
            max_pos = pos
    memory_banks[max_pos] = 0
    for pos in count(max_pos + 1):
        if max_mem == 0:
            break
        max_mem -= 1
        memory_banks[pos % len(memory_banks)] += 1
    return tuple(memory_banks)


def main():
    with open("memory.txt") as f:
        memory_banks = tuple(map(int, f.read().split()))

    seen = {}
    n_steps = 0
    while memory_banks not in seen:
        seen[memory_banks] = n_steps
        memory_banks = balance(memory_banks)
        n_steps += 1
    print(n_steps)
    print(n_steps - seen[memory_banks])


if __name__ == "__main__":
    main()
