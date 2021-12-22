from collections import Counter
from itertools import product
from functools import lru_cache

import numpy as np


def new_pos(pos, roll):
    return (pos + roll - 1) % 10 + 1


def main():
    player_1, player_2 = 7, 8
    rolls = Counter(map(sum, product((1, 2, 3), repeat=3)))

    @lru_cache(maxsize=None)
    def win_counts(pos_1, score_1, pos_2, score_2):
        if score_1 >= 21:
            return np.array([1, 0])
        if score_2 >= 21:
            return np.array([0, 1])

        wins = np.array([0, 0])
        for roll_1, count_1 in rolls.items():
            new_pos_1 = new_pos(pos_1, roll_1)
            new_score_1 = score_1 + new_pos_1
            if new_score_1 >= 21:
                wins[0] += count_1
            else:
                for roll_2, count_2 in rolls.items():
                    new_pos_2 = new_pos(pos_2, roll_2)
                    new_score_2 = score_2 + new_pos_2
                    wins += (
                        count_1
                        * count_2
                        * win_counts(new_pos_1, new_score_1, new_pos_2, new_score_2)
                    )
        return wins

    print(max(win_counts(player_1, 0, player_2, 0)))


if __name__ == "__main__":
    main()
