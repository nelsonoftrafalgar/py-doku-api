import numpy as np


class Validator:
    def __init__(self):
        self.sector_borders = [
            (0, 3, 0, 3),
            (0, 3, 3, 6),
            (0, 3, 6, 9),
            (3, 6, 0, 3),
            (3, 6, 3, 6),
            (3, 6, 6, 9),
            (6, 9, 0, 3),
            (6, 9, 3, 6),
            (6, 9, 6, 9)
        ]

    def validate_board(self, board):
        return self.validate_cols(board) and self.validate_rows(board) and self.validate_sectors(board)

    def validate_rows(self, board):
        return all([len(np.unique(board[i])) == 9 for i in range(9)])

    def validate_cols(self, board):
        return all([len(np.unique(board[:, i])) == 9 for i in range(9)])

    def validate_sectors(self, board):
        return all([len(np.unique(board[a:b, c:d])) == 9 for a, b, c, d in self.sector_borders])
