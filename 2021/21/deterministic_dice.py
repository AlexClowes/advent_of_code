from itertools import cycle


def new_pos(pos, dice_roll):
    return (pos + dice_roll - 1) % 10 + 1


def main():
    player_1, player_2 = 7, 8
    score_1 = score_2 = 0

    count = 0
    die = cycle(range(1, 101))

    def roll():
        nonlocal count
        count += 3
        return sum(next(die) for _ in range(3))

    while True:
        player_1 = new_pos(player_1, roll())
        score_1 += player_1
        if score_1 >= 1000:
            print(score_2 * count)
            return
        player_2 = new_pos(player_2, roll())
        score_2 += player_2
        if score_2 >= 1000:
            print(score_1 * count)
            return


if __name__ == "__main__":
    main()
