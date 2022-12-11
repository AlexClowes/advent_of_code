from collections import deque
from functools import reduce, cached_property
from operator import add, mul
import re
import textwrap


class Monkey:
    def __init__(self, monkeys, desc):
        self.monkeys = monkeys

        pat = textwrap.dedent("""\
            Monkey (?P<idx>\d+):
              Starting items: (?P<items>(?:\d+(?:,\s)?)*)
              Operation: new = old (?P<op>\+|\*) (?P<oparg>(?:\d+|old))
              Test: divisible by (?P<divisor>\d+)
                If true: throw to monkey (?P<truedest>\d+)
                If false: throw to monkey (?P<falsedest>\d+)"""
        )
        params = re.match(pat, desc).groupdict()

        self.idx = int(params["idx"])

        self.items = deque(map(int, params["items"].split(", ")))

        op = {"+": add, "*": mul}[params["op"]]
        self.operation = lambda old: op(
            old, old if params["oparg"] == "old" else int(params["oparg"])
        ) % self.modulo

        self.divisor = int(params["divisor"])
        test = lambda n: n % self.divisor == 0
        truedest = int(params["truedest"])
        falsedest = int(params["falsedest"])
        self.destination = lambda n: truedest if test(n) else falsedest

        self.activity_level = 0

    @cached_property
    def modulo(self):
        return reduce(mul, (monkey.divisor for monkey in self.monkeys))

    def catch(self, item):
        self.items.append(item)

    def throw(self, monkey_idx, item):
        self.monkeys[monkey_idx].catch(item)

    def take_turn(self):
        while self.items:
            self.activity_level += 1
            new_item = self.operation(self.items.popleft())
            self.throw(self.destination(new_item), new_item)


def main():
    monkeys = []
    with open("monkeys.txt") as f:
        for idx, desc in enumerate(f.read().split("\n\n")):
            monkeys.append(Monkey(monkeys, desc))
            assert idx == monkeys[-1].idx

    for _ in range(10000):
        for monkey in monkeys:
            monkey.take_turn()

    print(mul(*sorted(monkey.activity_level for monkey in monkeys)[-2:]))


if __name__ == "__main__":
    main()
