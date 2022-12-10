class Machine:
    def __init__(self):
        self.cycle = 0
        self.x = 1

    def _inc_cycle_and_yield(self):
        self.cycle += 1
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

    @property
    def signal_strength(self):
        return self.cycle * self.x


def main():
    cycles = [c for s in range(20, 221, 40) for c in (s - 1, s, s + 1)]
    with open("program.txt") as f:
        program = (line.strip().split() for line in f)
        states = Machine().run_program(program)
        print(sum(state.signal_strength for state in states if state.cycle % 40 == 20))


if __name__ == "__main__":
    main()

