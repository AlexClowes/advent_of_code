from collections import defaultdict
from itertools import cycle
import re


def main():
    with open("instructions.txt") as f:
        instructions = [line.strip() for line in f]

    loc2val = defaultdict(list)

    # Initialise bots
    for instr in instructions:
        if instr.startswith("value"):
            val, bot = re.match(r"value (\d+) goes to (bot \d+)", instr).groups()
            loc2val[bot].append(int(val))
    instructions = [instr for instr in instructions if not instr.startswith("value")]


    def make_bot(name, *destinations):
        def bot():
            self_vals = loc2val[name]
            if len(self_vals) == 2:
                self_vals = sorted(self_vals)
                if self_vals == [17, 61]:
                    print(name)
                for val, dest in zip(self_vals, destinations):
                    loc2val[dest].append(val)
                loc2val[name] = []
        return bot

    pat = r"(bot \d+) gives low to (\w+ \d+) and high to (\w+ \d+)"
    bots = [make_bot(*re.match(pat, instr).groups()) for instr in instructions]

    while any(loc.startswith("bot") and len(vals) == 2 for loc, vals in loc2val.items()):
        for b in bots:
            b()

    print(loc2val["output 0"][0] * loc2val["output 1"][0] * loc2val["output 2"][0])



if __name__ == "__main__":
    main()

