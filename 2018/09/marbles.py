from collections import deque


def high_score(n_players, n_marbles):
    marbles = deque((0,))
    scores = [0] * n_players
    for i in range(1, n_marbles + 1):
        if i % 23 != 0:
            marbles.append(marbles.popleft())
            marbles.append(i)
        else:
            player = (i - 1) % n_players
            scores[player] += i
            for _ in range(7):
                marbles.appendleft(marbles.pop())
            scores[player] += marbles.pop()
            marbles.append(marbles.popleft())
    return max(scores)


def main():
    print(high_score(418, 70769))
    print(high_score(418, 7076900))


if __name__ == "__main__":
    main()
