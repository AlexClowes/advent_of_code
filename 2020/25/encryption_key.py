def get_loop(subject_no, public_key, mod):
    n = 1
    loop = 0
    while n != public_key:
        n = (n * subject_no) % mod
        loop += 1
    return loop


def main():
    card_public_key = 15628416
    door_public_key = 11161639
    subject_no = 7
    mod = 20201227

    card_loop = get_loop(subject_no, card_public_key, mod)
    print(pow(door_public_key, card_loop, mod))


if __name__ == "__main__":
    main()
