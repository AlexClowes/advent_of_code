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


def pad(modes, expected_len):
    modes += [0] * (expected_len - len(modes))


def convert_read_params(params, param_modes, program, relative_base):
    for i, mode in enumerate(param_modes):
        if mode == 0:
            params[i] = program[params[i]]
        elif mode == 2:
            params[i] = program[params[i] + relative_base]
    return params


def convert_write_param(param, param_mode, relative_base):
    if param_mode == 2:
        return param + relative_base
    return param


@coroutine
def int_code_computer(program):
    program = list(program) + [0] * 1024
    pos = 0
    relative_base = 0
    while True:
        # Get op code and parameter modes
        op_code, param_modes = decode(program[pos])
        if op_code in [1, 2, 7, 8]:
            # Binary operations
            pad(param_modes, 3)
            params = program[pos + 1 : pos + 4]
            params[:2] = convert_read_params(
                params[:2], param_modes[:2], program, relative_base
            )
            params[2] = convert_write_param(params[2], param_modes[2], relative_base)
            program[params[2]] = int({1: add, 2: mul, 7: lt, 8: eq}[op_code](*params[:2]))
            pos += 4
        elif op_code == 3:
            # Input
            pad(param_modes, 1)
            param = convert_write_param(program[pos + 1], param_modes[0], relative_base)
            program[param] = yield
            pos += 2
        elif op_code == 4:
            # Output
            pad(param_modes, 1)
            yield convert_read_params(
                program[pos + 1 : pos + 2], param_modes, program, relative_base
            )[0]
            pos += 2
        elif op_code in [5, 6]:
            # Jump if true / false
            pad(param_modes, 2)
            params = program[pos + 1 : pos + 3]
            params = convert_read_params(params, param_modes, program, relative_base)
            if (op_code == 5 and params[0]) or (op_code == 6 and not params[0]):
                pos = params[1]
            else:
                pos += 3
        elif op_code == 9:
            # Change relative base
            pad(param_modes, 1)
            param = convert_read_params(
                program[pos + 1 : pos + 2], param_modes, program, relative_base
            )[0]
            relative_base += param
            pos += 2
        elif op_code == 99:
            break
        else:
            raise ValueError(f"Unrecognised op code {op_code}")
