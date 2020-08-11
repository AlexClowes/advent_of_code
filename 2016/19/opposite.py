def f(n):
    ret = 1
    for i in range(2, n + 1):
        ret += 1
        if ret >= (i + 1) / 2:
            ret += 1
        if ret > i:
            ret -= i
    return ret


def main():
    print(f(3018458))


if __name__ == "__main__":
    main()
