import numpy as np


def display(state):
    print("\n".join("".join(".#"[val] for val in row[1:-1]) for row in state[1:-1]))


def update(state):
    new_state = np.zeros_like(state)
    for i in range(1, state.shape[0] - 1):
        for j in range(1, state.shape[1] - 1):
            neighbour_count = np.sum(state[i-1:i+2, j-1:j+2]) - state[i, j]
            if state[i, j]:
                new_state[i, j] = (neighbour_count in (2, 3))
            else:
                new_state[i, j] = (neighbour_count == 3)
    return new_state


def main():
    state = np.zeros((102, 102), dtype=np.bool)
    with open("initial_state.txt") as f:
        for i, line in enumerate(f, 1):
            for j, char in enumerate(line.strip(), 1):
                state[i, j] = 1 if char == "#" else 0

    for _ in range(100):
        state = update(state)
    print(np.sum(state))


if __name__ == "__main__":
    main()
