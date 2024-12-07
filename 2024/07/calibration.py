from operator import add, mul


def concat(x, y):
    return int(str(x) + str(y))


def is_possible(ops, target, *args):
    def recurse(*args):
        if len(args) == 1:
            return target == args[0]
        first, second, *rest = args
        for op in ops:
            new_first = op(first, second)
            if new_first <= target and recurse(new_first, *rest):
                return True
        return False
    return recurse(*args)


def main():
    with open("equations.txt") as f:
        part_1 = part_2 = 0
        for line in f:
            target,  args = line.strip().split(": ")
            target = int(target)
            args = [int(arg) for arg in args.split()]
            if is_possible((add, mul), target, *args):
                part_1 += target
                part_2 += target
            elif is_possible((add, mul, concat), target, *args):
                part_2 += target
    print(part_1)
    print(part_2)


if __name__ == "__main__":
    main()
