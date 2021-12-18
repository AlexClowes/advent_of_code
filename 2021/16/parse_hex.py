from enum import Enum
from collections import namedtuple
from itertools import chain
from math import prod
from operator import eq, gt, lt


HEX2BIN = {
    "0": (0, 0, 0, 0),
    "1": (0, 0, 0, 1),
    "2": (0, 0, 1, 0),
    "3": (0, 0, 1, 1),
    "4": (0, 1, 0, 0),
    "5": (0, 1, 0, 1),
    "6": (0, 1, 1, 0),
    "7": (0, 1, 1, 1),
    "8": (1, 0, 0, 0),
    "9": (1, 0, 0, 1),
    "A": (1, 0, 1, 0),
    "B": (1, 0, 1, 1),
    "C": (1, 1, 0, 0),
    "D": (1, 1, 0, 1),
    "E": (1, 1, 1, 0),
    "F": (1, 1, 1, 1),
}


class TypeID(Enum):
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    CONSTANT = 4
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL_TO = 7


class BitStream:
    def __init__(self, hexdump):
        self.bits = chain.from_iterable(HEX2BIN[h] for h in hexdump)
        self.pos = 0

    def __next__(self):
        bit = next(self.bits)
        self.pos += 1
        return bit


Packet = namedtuple("Packet", ["version", "type_id", "data"])


def parse(bits):
    def get_int(n_digits):
        ret = 0
        for _ in range(n_digits):
            ret = (ret << 1) + next(bits)
        return ret

    version = get_int(3)
    type_id = TypeID(get_int(3))
    if type_id == TypeID.CONSTANT:
        data = 0
        not_done = True
        while not_done:
            not_done = get_int(1)
            data = (data << 4) + get_int(4)
    else:
        if get_int(1) == 0:
            n_bits = get_int(15)
            sub_packets_end = bits.pos + n_bits
            data = []
            while bits.pos != sub_packets_end:
                data.append(parse(bits))
        else:
            data = [parse(bits) for _ in range(get_int(11))]
    return Packet(version, type_id, data)


def sum_version_nos(packet):
    total = packet.version
    if isinstance(packet.data, list):
        for sub_packet in packet.data:
            total += sum_version_nos(sub_packet)
    return total


def evaluate(packet):
    if isinstance(packet.data, int):
        return packet.data
    return {
        TypeID.SUM: sum,
        TypeID.PRODUCT: prod,
        TypeID.MINIMUM: min,
        TypeID.MAXIMUM: max,
        TypeID.GREATER_THAN: lambda args: gt(*args),
        TypeID.LESS_THAN: lambda args: lt(*args),
        TypeID.EQUAL_TO: lambda args: eq(*args),
    }[packet.type_id](map(evaluate, packet.data))


def main():
    with open("hexdump.txt") as f:
        packet = parse(BitStream(f.read().strip()))
    # Part 1
    print(sum_version_nos(packet))
    # Part 2
    print(evaluate(packet))


if __name__ == "__main__":
    main()
