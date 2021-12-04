import numpy as np


class BingoBoard:
    def __init__(self, board):
        self.board = np.array(board)
        self.mark = np.zeros_like(self.board, dtype=bool)
        self.last_num = None

    def check(self, number):
        self.last_num = number
        self.mark[self.board == number] = True
        return np.any(np.all(self.mark, axis=0)) or np.any(np.all(self.mark, axis=1))

    def score(self):
        return np.sum(self.board[~self.mark]) * self.last_num


def main():
    with open("boards.txt") as f:
        numbers = map(int, next(f).split(","))
        f.readline()  # Empty line
        boards = [
            BingoBoard(
                [list(map(int, row.split())) for row in board_string.split("\n")]
            )
            for board_string in f.read().strip().split("\n\n")
        ]

    for num in numbers:
        for i, board in enumerate(boards):
            if board.check(num):
                print(board.score())
                return


if __name__ == "__main__":
    main()
