from collections import defaultdict
import re


def transition(new_val, movement, new_state):
    def func(tape, pos):
        tape[pos] = new_val
        new_pos = pos + (1 if movement == "right" else -1)
        return new_state, new_pos
    return func


def parse_program(program):
    initial_state = re.match(r"Begin in state (\w).", program[0][0]).group(1)
    n_steps = int(
        re.match(
            r"Perform a diagnostic checksum after (\d+) steps.", program[0][1]
        ).group(1)
    )

    transitions = {}
    for paragraph in program[1:]:
        state = re.match(r"In state (\w).", paragraph[0]).group(1)
        for value, block in enumerate((paragraph[2:5], paragraph[6:9])):
            new_val = int(re.search(r"Write the value (0|1).", block[0]).group(1))
            movement = re.search(r"Move one slot to the (right|left).", block[1]).group(1)
            new_state = re.search(r"Continue with state (\w).", block[2]).group(1)
            transitions[state, value] = transition(new_val, movement, new_state)

    return initial_state, n_steps, transitions


def run(program):
    state, n_steps, transitions = parse_program(program)
    tape = defaultdict(int)
    pos = 0
    for _ in range(n_steps):
        state, pos = transitions[state, tape[pos]](tape, pos)
    return sum(tape.values())


def main():
    with open("program.txt") as f:
        program = [para.split("\n") for para in f.read().split("\n\n")]
    print(run(program))


if __name__ == "__main__":
    main()
