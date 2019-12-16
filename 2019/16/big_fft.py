from itertools import cycle, repeat


def cheat_fft(in_signal):
    out_signal = [0] * len(in_signal)
    out_signal[-1] = in_signal[-1]
    for i in range(len(out_signal) - 2, -1, -1):
        out_signal[i] = abs(out_signal[i + 1] + in_signal[i]) % 10
    return out_signal


def main():
    with open("signal.txt") as f:
        signal = f.readline().strip()
    offset = int(signal[:7])

    # Optimisation only works if assertion holds
    assert 2 * offset > len(signal)

    signal = [int(n) for n in (signal * 10000)[offset:]]

    for _ in range(100):
        signal = cheat_fft(signal)
    print("".join(map(str, signal[:8])))


if __name__ == "__main__":
    main()
