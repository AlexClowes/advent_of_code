import numpy as np


class Machine:
    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.screen = np.zeros((6, 40), dtype=bool)

    def _inc_cycle_and_yield(self):
        self.cycle += 1
        self.draw()
        yield self

    def run(self, instr):
        match instr:
            case "noop",:
                yield from self._inc_cycle_and_yield()
            case "addx", n:
                yield from self._inc_cycle_and_yield()
                yield from self._inc_cycle_and_yield()
                self.x += int(n)

    def run_program(self, program):
        yield self
        for instr in program:
            yield from self.run(instr)

    def draw(self):
        pixel = divmod(self.cycle - 1, self.screen.shape[1])
        self.screen[pixel] = abs(self.x - pixel[1]) <= 1

    def display(self):
        return "\n".join(
            "".join("#" if p else " " for p in line) for line in self.screen
        )


def main():
    cycles = [c for s in range(20, 221, 40) for c in (s - 1, s, s + 1)]
    with open("program.txt") as f:
        program = (line.strip().split() for line in f)
        *_, final = Machine().run_program(program)
        print(final.display())


if __name__ == "__main__":
    main()

