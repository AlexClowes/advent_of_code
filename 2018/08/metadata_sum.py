def recurse(data):
    n_children, n_metadata = next(data), next(data)
    metadata_sum = 0
    value = 0
    child_vals = []
    for _ in range(n_children):
        child_metadata_sum, child_value = recurse(data)
        metadata_sum += child_metadata_sum
        child_vals.append(child_value)
    for _ in range(n_metadata):
        metadata = next(data)
        metadata_sum += metadata
        if 0 < metadata <= n_children:
            value += child_vals[metadata - 1]
    if n_children == 0:
        value = metadata_sum
    return metadata_sum, value


def main():
    with open("data.txt") as f:
        data = map(int, f.read().strip().split())
        metadata_sum, value = recurse(data)
        print(metadata_sum)
        print(value)


if __name__ == "__main__":
    main()
