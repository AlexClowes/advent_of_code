from operator import add, eq, lt, mul


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


def decode(instruction):
    op_code = instruction % 100
    instruction //= 100
    param_modes = []
    while instruction > 0:
        param_modes.append(instruction % 10)
        instruction //= 10
    return op_code, param_modes


def convert_params(params, param_modes, program):
    param_modes += [0] * (len(params) - len(param_modes))
    for i, mode in enumerate(param_modes):
        if mode == 0:
            params[i] = program[params[i]]
    return params


@coroutine
def int_code_computer(program):
    program = list(program)
    pos = 0
    output = None
    while True:
        # Get op code and parameter modes
        op_code, param_modes = decode(program[pos])
        if op_code in [1, 2, 7, 8]:
            # Binary operations
            params = program[pos + 1: pos + 4]
            params[:2] = convert_params(params[:2], param_modes[:2], program)
            program[params[2]] = {1: add, 2: mul, 7: lt, 8: eq}[op_code](*params[:2])
            pos += 4
        elif op_code == 3:
            # Input
            program[program[pos + 1]] = yield output
            pos += 2
        elif op_code == 4:
            # Output
            if not param_modes or param_modes[0] == 0:
                output = program[program[pos + 1]]
            else:
                output = program[pos + 1]
            pos += 2
        elif op_code in [5, 6]:
            # Jump if true / false
            params = program[pos + 1: pos + 3]
            params = convert_params(params, param_modes, program)
            if (op_code == 5 and params[0]) or (op_code == 6 and not params[0]):
                pos = params[1]
            else:
                pos += 3
        elif op_code == 99:
            yield output
            break
        else:
            raise ValueError(f"Unrecognised op code {op_code}")
