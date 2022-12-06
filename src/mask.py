from random import random
import numpy as np
from py_doku.src.generator import Generator


class Mask:
    def __init__(self):
        generator = Generator()
        self.valid_board = generator.generate_valid_board()

    def mask_board(self, level):
        masked_board = []
        for x in range(9):
            x_list = []
            for y in range(9):
                if random() > level:
                    x_list.append(None)
                else:
                    x_list.append(str(self.valid_board[x][y]))
            masked_board.append(x_list)
        return masked_board
