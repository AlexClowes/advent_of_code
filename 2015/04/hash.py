from hashlib import md5


def main():
    secret_key = "bgvyzdsv"
    n = 1
    while md5((secret_key + str(n)).encode("ascii")).hexdigest()[:5] != "00000":
        n += 1
    print(n)

    print()

    n = 1
    while md5((secret_key + str(n)).encode("ascii")).hexdigest()[:6] != "000000":
        n += 1
    print(n)



if __name__ == "__main__":
    main()
