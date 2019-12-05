import operator


class IntCodeComputer:
    def __init__(self, program):
        self.pos = 0
        self.program = program

    @staticmethod
    def decode(instruction):
        op_code = instruction % 100
        instruction //= 100
        param_modes = []
        while instruction > 0:
            param_modes.append(instruction % 10)
            instruction //= 10
        return op_code, param_modes

    @staticmethod
    def pad(modes, expected_len):
        modes += [0] * (expected_len - len(modes))

    def bin_op(self, param_modes, args, operator):
        self.pad(param_modes, 3)
        for i in range(2):
            if param_modes[i] == 0:
                args[i] = self.program[args[i]]
        assert param_modes[2] == 0
        self.program[args[2]] = operator(*args[:2])

    def add(self, param_modes, args):
        self.bin_op(param_modes, args, operator.add)
    
    def mult(self, param_modes, args):
        self.bin_op(param_modes, args, operator.mul)

    def read_in(self, param_modes, args, in_val):
        self.pad(param_modes, 1)
        assert param_modes[0] == 0
        self.program[args[0]] = in_val

    def write_out(self, param_modes, args):
        self.pad(param_modes, 1)
        if param_modes[0] == 0:
            args[0] = self.program[args[0]]
        print(args[0])

    def jump_if_true(self, param_modes, args):
        self.pad(param_modes, 2)
        for i in range(2):
            if param_modes[i] == 0:
                args[i] = self.program[args[i]]
        if args[0]:
            self.pos = args[1]
        else:
            self.pos += 3

    def jump_if_false(self, param_modes, args):
        self.pad(param_modes, 2)
        for i in range(2):
            if param_modes[i] == 0:
                args[i] = self.program[args[i]]
        if not args[0]:
            self.pos = args[1]
        else:
            self.pos += 3

    def less_than(self, param_modes, args):
        self.bin_op(param_modes, args, lambda x, y: int(x < y))

    def equals(self, param_modes, args):
        self.bin_op(param_modes, args, lambda x, y: int(x == y))

    def instructions(self):
        while True:
            op_code, _ = self.decode(self.program[self.pos])
            if op_code in [1, 2, 7, 8]:
                yield self.program[self.pos : self.pos + 4]
                self.pos += 4
            elif op_code in [3, 4]:
                yield self.program[self.pos : self.pos + 2]
                self.pos += 2
            elif op_code in [5, 6]:
                yield self.program[self.pos : self.pos + 3]
            elif op_code in [99]:
                yield self.program[self.pos : self.pos + 1]
                self.pos += 1
            else:
                raise ValueError(f"Unrecognised op code {op_code}")

    def run(self, in_val):
        for instruction in self.instructions():
            op, *args = instruction
            op_code, param_modes = self.decode(op)
            if op_code == 1:
                self.add(param_modes, args)
            elif op_code == 2:
                self.mult(param_modes, args)
            elif op_code == 3:
                self.read_in(param_modes, args, in_val)
            elif op_code == 4:
                self.write_out(param_modes, args)
            elif op_code == 5:
                self.jump_if_true(param_modes, args)
            elif op_code == 6:
                self.jump_if_false(param_modes, args)
            elif op_code == 7:
                self.less_than(param_modes, args)
            elif op_code == 8:
                self.equals(param_modes, args)
            elif op_code == 99:
                break
            else:
                raise ValueError(f"Unrecognised op code {op_code}")
