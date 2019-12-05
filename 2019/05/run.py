import operator


def instruction_gen(program):
    pos = 0
    while True:
        op_code, _ = decode(program[pos])
        if op_code in [1, 2]:
            yield program[pos : pos + 4]
            pos += 4
        elif op_code in [3, 4]:
            yield program[pos : pos + 2]
            pos += 2
        elif op_code in [99]:
            yield program[pos : pos + 1]
            pos += 1
        else:
            raise ValueError(f"Unrecognised op code {op_code}")


def decode(instruction):
    op_code = instruction % 100
    instruction //= 100
    param_modes = []
    while instruction > 0:
        param_modes.append(instruction % 10)
        instruction //= 10
    return op_code, param_modes


def pad(modes, expected_len):
    modes += [0] * (expected_len - len(modes))


def bin_op(program, param_modes, args, operator):
    pad(param_modes, 3)
    for i in range(2):
        if param_modes[i] == 0:
            args[i] = program[args[i]]
    assert param_modes[2] == 0
    program[args[2]] = operator(*args[:2])


def add(program, param_modes, args):
    bin_op(program, param_modes, args, operator.add)


def mult(program, param_modes, args):
    bin_op(program, param_modes, args, operator.mul)


def read_in(program, param_modes, args, in_val):
    pad(param_modes, 1)
    assert param_modes[0] == 0
    program[args[0]] = in_val


def write_out(program, param_modes, args):
    pad(param_modes, 1)
    if param_modes[0] == 0:
        args[0] = program[args[0]]
    print(args[0])


def run(program, in_val):
    for instruction in instruction_gen(program):
        op, *args = instruction
        op_code, param_modes = decode(op)
        if op_code == 1:
            add(program, param_modes, args)
        elif op_code == 2:
            mult(program, param_modes, args)
        elif op_code == 3:
            read_in(program, param_modes, args, in_val)
        elif op_code == 4:
            write_out(program, param_modes, args)
        elif op_code == 99:
            break
        else:
            raise ValueError(f"Unrecognised op code {op_code}")


def main():
    with open("program.txt") as f:
        program = list(map(int, f.readline().split(",")))
    run(program, 1)


if __name__ == "__main__":
    main()
