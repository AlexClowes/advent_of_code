def main():
    skip_size = 359
    buf = []
    pos = 0
    for i in range(2018):
        buf.insert(pos + 1, i)
        pos = (pos + skip_size + 1) % len(buf)

    print(buf[buf.index(2017) + 1])


if __name__ == "__main__":
    main()
