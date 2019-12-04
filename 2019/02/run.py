from operator import add, mul


def run_program(program):
    pos = 0
    while program[pos] != 99:
        if program[pos] == 1:
            op = add
        elif program[pos] == 2:
            op = mul
        else:
            raise ValueError
        arg1 = program[program[pos + 1]]
        arg2 = program[program[pos + 2]]
        program[program[pos + 3]] = op(arg1, arg2)
        pos += 4
    return program
