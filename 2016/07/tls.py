import re


def has_abba(block):
    return any(
        c0 != c1 and c0 == c3 and c1 == c2
        for c0, c1, c2, c3 in zip(*(block[i:] for i in range(4)))
    )


def supports_tls(ip_address):
    blocks = re.findall(r"\w+", ip_address)
    return (
        any(has_abba(b) for b in blocks[::2])
        and not any(has_abba(b) for b in blocks[1::2])
    )


def main():
    with open("ip_addresses.txt") as f:
        print(sum(supports_tls(addr.strip()) for addr in f))


if __name__ == "__main__":
    main()
