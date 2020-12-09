def find_invalid(data, preamble_len):
    preamble = set(data[:preamble_len])
    for i, n in enumerate(data[preamble_len:], preamble_len):
        if all(n - p not in preamble for p in preamble):
            break
        preamble.remove(data[i - preamble_len])
        preamble.add(n)
    return n


def find_contig_range(data, target):
    lo, hi = 0, 0
    total = data[0]
    while total != target:
        if lo == hi or total < target:
            hi += 1
            total += data[hi]
        else:
            total -= data[lo]
            lo += 1
    return data[lo : hi + 1]


def main():
    with open("data.txt") as f:
        data = [int(line.strip()) for line in f]

    invalid = find_invalid(data, 25)
    print(invalid)

    contig_range = find_contig_range(data, invalid)
    print(min(contig_range) + max(contig_range))


if __name__ == "__main__":
    main()
