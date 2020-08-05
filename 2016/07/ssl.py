from itertools import chain
import re


def gen_aba(block):
    return (
        (c0, c1) for c0, c1, c2 in zip(block, block[1:], block[2:]) if c1 != c0 == c2
    )


def supports_ssl(ip_address):
    blocks = re.findall(r"\w+", ip_address)
    aba = set(chain.from_iterable(gen_aba(b) for b in blocks[::2]))
    bab = chain.from_iterable(gen_aba(b) for b in blocks[1::2])
    return any((a, b) in aba for b, a in bab)


def main():
    with open("ip_addresses.txt") as f:
        print(sum(supports_ssl(addr.strip()) for addr in f))


if __name__ == "__main__":
    main()
