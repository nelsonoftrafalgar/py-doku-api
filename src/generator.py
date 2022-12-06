import numpy as np
from py_doku.src.pydoku import Pydoku
from py_doku.src.validator import Validator


class Generator:
    def __init__(self):
        self.pydoku = Pydoku()
        self.validator = Validator()

    def iterate_rows(self, y):
        for x in range(9):
            current_number = self.pydoku.raw_board[y][x]
            previous_in_row = self.pydoku.get_previous_in_row((x, y))

            if current_number in previous_in_row:
                if y > x:
                    self.handle_sorted_col_swap(
                        x, y, previous_in_row, current_number)
                else:
                    available_numbers = self.pydoku.get_row_available_numbers(
                        (x, y), current_number)
                    unavailable = self.pydoku.get_unavailable_for_row(x, y)
                    numbers = available_numbers[:, unavailable:]
                    row, col = np.where(
                        np.isin(numbers, previous_in_row, invert=True))
                    if len(row) == 0 or len(col) == 0:
                        self.handle_row_swap(y, x, current_number)
                    else:
                        self.handle_single_swap(numbers, row, col, x, y)

    def iterate_cols(self, x):
        for y in range(9):
            current_number = self.pydoku.raw_board[y][x]
            previous_in_col = self.pydoku.get_previous_in_col((x, y))

            if current_number in previous_in_col:
                if x >= y:
                    self.handle_sorted_row_swap(
                        x, y, previous_in_col, current_number)
                else:
                    available_numbers = self.pydoku.get_col_available_numbers(
                        (x, y), current_number)
                    unavailable = self.pydoku.get_unavailable_for_col(x, y)
                    numbers = available_numbers[unavailable:]
                    row, col = np.where(
                        np.isin(numbers, previous_in_col, invert=True))
                    if len(row) == 0 or len(col) == 0:
                        self.handle_col_swap(y, x, current_number)
                    else:
                        self.handle_single_swap(numbers, row, col, x, y)

    def iterator(self, start):
        if start > 8:
            return

        self.iterate_rows(start)
        self.iterate_cols(start)
        self.iterator(start + 1)

    def handle_sorted_col_swap(self, x, y, previous_in_row, current_number):
        adjacent = self.pydoku.raw_board[y:, x:x+1][0]
        available_numbers = adjacent[~np.in1d(
            adjacent, previous_in_row)]
        if len(available_numbers) > 0:
            swap_position = np.argwhere(
                adjacent == available_numbers[0])
            adjacent[swap_position][0], adjacent[0] = adjacent[0], adjacent[swap_position][0]
        else:
            self.handle_row_swap(y, x, current_number)

    def handle_sorted_row_swap(self, x, y, previous_in_col, current_number):
        adjacent = self.pydoku.raw_board[y:y+1, x:][0]
        available_numbers = adjacent[~np.in1d(
            adjacent, previous_in_col)]
        if len(available_numbers) > 0:
            swap_position = np.argwhere(
                adjacent == available_numbers[0])
            adjacent[swap_position], adjacent[0] = adjacent[0], adjacent[swap_position]
        else:
            self.handle_col_swap(y, x, current_number)

    def handle_single_swap(self, numbers, row, col, x, y):
        self.pydoku.raw_board[y][x], numbers[row[0]][col[0]
                                                     ] = numbers[row[0]][col[0]], self.pydoku.raw_board[y][x]

    def handle_row_swap(self, y, x, current_number):
        swap_matrix = self.pydoku.raw_board[y:y+2, :x]
        swap_col = np.where(swap_matrix[0] == current_number)[0][0]

        def flip_col(col):
            swap_matrix[:, col] = np.flip(swap_matrix[:, col])

        flip_col(swap_col)

        def swap_rows(col):
            conflict_list = np.where(
                swap_matrix[0] == swap_matrix[0][col])[0]
            if len(conflict_list) == 1:
                return

            col = np.delete(conflict_list, np.argwhere(
                conflict_list == col))[0]
            flip_col(col)
            swap_rows(col)

        swap_rows(swap_col)
        self.pydoku.raw_board[y:y+2, :x] = swap_matrix

    def handle_col_swap(self, y, x, current_number):
        swap_matrix = self.pydoku.raw_board[:y, x:x+2]
        swap_row = np.where(swap_matrix[:y, 0] == current_number)[0][0]

        def flip_row(row):
            swap_matrix[row] = np.flip(swap_matrix[row])

        flip_row(swap_row)

        def swap_cols(row):
            conflict_list = np.where(
                swap_matrix[:y, 0] == swap_matrix[:y, 0][row])[0]
            if len(conflict_list) == 1:
                return

            row = np.delete(conflict_list, np.argwhere(
                conflict_list == row))[0]
            flip_row(row)
            swap_cols(row)

        swap_cols(swap_row)
        self.pydoku.raw_board[:y, x:x+2] = swap_matrix

    def generate_valid_board(self):
        is_valid = self.validator.validate_board(self.pydoku.raw_board)

        while not is_valid:
            self.pydoku = Pydoku()
            self.iterator(0)
            is_valid = self.validator.validate_board(self.pydoku.raw_board)

        return self.pydoku.raw_board
