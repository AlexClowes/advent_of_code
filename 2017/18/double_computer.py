from collections import defaultdict
import operator
from queue import Queue


def prog(program, program_id, snd_queue, rcv_queue):
    registers = defaultdict(int)
    registers["p"] = program_id
    value = lambda x: registers[x] if x.isalpha() else int(x)
    instruction_pointer = 0
    while 0 <= instruction_pointer < len(program):
        op, *args = program[instruction_pointer].split()
        if op == "set":
            registers[args[0]] = value(args[1])
        elif op in ("add", "mul", "mod"):
            func = getattr(operator, op)
            registers[args[0]] = func(registers[args[0]], value(args[1]))
        elif op == "jgz":
            if value(args[0]) > 0:
                instruction_pointer += value(args[1]) - 1
        elif op == "snd":
            snd_queue.put(value(args[0]))
            yield True
        elif op == "rcv":
            if rcv_queue.empty():
                instruction_pointer -= 1
                yield False
            else:
                registers[args[0]] = rcv_queue.get()
        instruction_pointer += 1


def count_sends_before_blocking(prog):
    ret = 0
    while next(prog):
        ret += 1
    return ret


def run(program):
    q0, q1 = Queue(), Queue()
    prog0 = prog(program, 0, q0, q1)
    prog1 = prog(program, 1, q1, q0)

    total = 0
    while True:
        prog0_sends = count_sends_before_blocking(prog0)
        prog1_sends = count_sends_before_blocking(prog1)
        total += prog1_sends
        if prog0_sends == prog1_sends == 0:
            return total


def main():
    with open("program.txt") as f:
        program = [line.strip() for line in f]
    print(run(program))


if __name__ == "__main__":
    main()
