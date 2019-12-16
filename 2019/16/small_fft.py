from itertools import cycle, repeat


def stencil(idx):
    for n in cycle([1, 0, -1, 0]):
        yield from repeat(n, idx + 1)


def fft(in_signal):
    out_signal = [0] * len(in_signal)
    for i in range(len(in_signal)):
        out_signal[i] = abs(sum(inp * st for inp, st in zip(in_signal[i:], stencil(i)))) % 10
    return out_signal


def main():
    with open("signal.txt") as f:
        signal = [int(n) for n in f.readline().strip()]
    for _ in range(100):
        signal = fft(signal)
    print("".join(map(str, signal[:8])))


if __name__ == "__main__":
    main()
