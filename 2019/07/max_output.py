from itertools import permutations

from computer import int_code_computer


def main():
    with open("amplifier_program.txt") as f:
        amplifier_program = [int(n) for n in f.readline().strip().split(",")]

    max_signal = 0
    for phase_setting in permutations(range(5)):
        computers = [int_code_computer(amplifier_program) for _ in range(5)]
        for phase, comp in zip(phase_setting, computers):
            comp.send(phase)
        signal = 0
        for comp in computers:
            signal = comp.send(signal)
        max_signal = max(signal, max_signal)
    print(max_signal)


if __name__ == "__main__":
    main()
