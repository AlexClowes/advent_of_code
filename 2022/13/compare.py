def parse(packet_str):
    pos = 0

    def get_int():
        nonlocal pos
        ret = 0
        while (char := packet_str[pos]) not in ",]":
            ret = 10 * ret + int(char)
            pos += 1
        return ret

    def get_list():
        nonlocal pos
        ret = []

        assert packet_str[pos] == "["
        pos += 1

        while (char := packet_str[pos]):
            match char:
                case "[":
                    ret.append(get_list())
                case ",":
                    pos += 1
                case "]":
                    pos += 1
                    return ret
                case other:
                    ret.append(get_int())

    return get_list()


def cmp_ints(left, right):
    return -1 if left < right else 1 if left > right else 0


def cmp_lists(left, right):
    for l, r in zip(left, right):
        if (c := cmp(l, r)) != 0:
            return c
    return cmp_ints(len(left), len(right))


def cmp(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return cmp_ints(left, right)
    if isinstance(left, list) and isinstance(right, list):
        return cmp_lists(left, right)
    if isinstance(left, int):
        return cmp([left], right)
    return cmp(left, [right])


def ordered(left, right):
    return cmp(left, right) == -1
    

def main():
    with open("packets.txt") as f:
        pairs = (
            map(parse, p.split("\n")) for p in f.read().strip().split("\n\n")
        )
        print(sum(i for i, (l, r) in enumerate(pairs, 1) if ordered(l, r)))


if __name__ == "__main__":
    main()
