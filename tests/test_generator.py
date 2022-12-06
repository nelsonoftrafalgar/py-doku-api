import pytest
import numpy as np
from py_doku.src.generator import Generator
from tests import TEST_BOARD


@pytest.fixture
def generator():
    return Generator()


def test_generate_valid_board(generator):
    generator.pydoku.raw_board = np.array(TEST_BOARD)
    generator.iterator(0)
    control_board = np.array([[2, 6, 3, 1, 5, 4, 7, 9, 8],
                              [4, 9, 1, 2, 7, 8, 3, 6, 5],
                              [5, 8, 7, 9, 6, 3, 1, 2, 4],
                              [8, 5, 6, 4, 3, 1, 9, 7, 2],
                              [7, 3, 9, 6, 8, 2, 4, 5, 1],
                              [1, 4, 2, 5, 9, 7, 6, 8, 3],
                              [9, 1, 5, 8, 4, 6, 2, 3, 7],
                              [3, 2, 8, 7, 1, 9, 5, 4, 6],
                              [6, 7, 4, 3, 2, 5, 8, 1, 9]])
    assert np.array_equal(generator.pydoku.raw_board, control_board)


def test_handle_sorted_col_swap(generator):
    generator.pydoku.raw_board = np.array([[2, 6, 3, 1, 5, 4, 7, 9, 8],
                                           [4, 9, 1, 2, 7, 8, 3, 6, 5],
                                           [5, 8, 7, 9, 6, 3, 1, 2, 4],
                                           [8, 5, 6, 4, 3, 1, 9, 2, 7],
                                           [7, 3, 9, 6, 8, 2, 4, 1, 5],
                                           [1, 4, 2, 5, 9, 7, 3, 6, 8],
                                           [6, 1, 8, 8, 4, 6, 2, 6, 4],
                                           [9, 2, 5, 3, 1, 9, 7, 8, 5],
                                           [3, 7, 4, 7, 2, 5, 3, 1, 9]])
    generator.handle_sorted_col_swap(3, 6, np.array([6, 1, 8]), 8)
    control_board = np.array([[2, 6, 3, 1, 5, 4, 7, 9, 8],
                              [4, 9, 1, 2, 7, 8, 3, 6, 5],
                              [5, 8, 7, 9, 6, 3, 1, 2, 4],
                              [8, 5, 6, 4, 3, 1, 9, 2, 7],
                              [7, 3, 9, 6, 8, 2, 4, 1, 5],
                              [1, 4, 2, 5, 9, 7, 3, 6, 8],
                              [6, 1, 5, 8, 4, 6, 2, 6, 4],
                              [9, 2, 8, 3, 1, 9, 7, 8, 5],
                              [3, 7, 4, 7, 2, 5, 3, 1, 9]])
    assert np.array_equal(generator.pydoku.raw_board, control_board)


def test_handle_sorted_row_swap(generator):
    generator.pydoku.raw_board = np.array([[2, 6, 3, 1, 5, 4, 7, 9, 8],
                                           [4, 9, 1, 2, 7, 8, 3, 6, 5],
                                           [5, 8, 7, 9, 6, 3, 1, 2, 4],
                                           [8, 5, 6, 4, 3, 1, 9, 2, 7],
                                           [7, 3, 9, 6, 8, 2, 4, 1, 5],
                                           [1, 4, 2, 5, 9, 7, 3, 6, 8],
                                           [9, 1, 5, 8, 4, 6, 2, 7, 3],
                                           [6, 2, 8, 3, 1, 9, 6, 8, 5],
                                           [3, 7, 4, 7, 2, 5, 4, 1, 9]])
    generator.handle_sorted_row_swap(6, 5, np.array([7, 3, 1, 9, 4]), 3)
    control_board = np.array([[2, 6, 3, 1, 5, 4, 7, 9, 8],
                              [4, 9, 1, 2, 7, 8, 3, 6, 5],
                              [5, 8, 7, 9, 6, 3, 1, 2, 4],
                              [8, 5, 6, 4, 3, 1, 9, 2, 7],
                              [7, 3, 9, 6, 8, 2, 4, 1, 5],
                              [1, 4, 2, 5, 9, 7, 6, 3, 8],
                              [9, 1, 5, 8, 4, 6, 2, 7, 3],
                              [6, 2, 8, 3, 1, 9, 6, 8, 5],
                              [3, 7, 4, 7, 2, 5, 4, 1, 9]])
    assert np.array_equal(generator.pydoku.raw_board, control_board)


def test_handle_single_swap(generator):
    generator.pydoku.raw_board = np.array([[2, 6, 3, 1, 2, 4, 5, 6, 8],
                                           [4, 9, 1, 5, 8, 9, 3, 4, 7],
                                           [5, 8, 7, 7, 6, 3, 1, 2, 9],
                                           [8, 5, 6, 5, 1, 3, 4, 1, 6],
                                           [7, 3, 4, 6, 4, 9, 9, 2, 3],
                                           [1, 9, 2, 2, 7, 8, 5, 7, 8],
                                           [4, 8, 1, 9, 1, 6, 2, 6, 4],
                                           [9, 6, 5, 3, 8, 4, 7, 8, 5],
                                           [3, 7, 2, 2, 7, 5, 3, 1, 9]])
    generator.handle_single_swap(np.array([[5, 8, 9], [7, 6, 3]]), [
                                 0, 0, 0, 1], [0, 1, 2, 0], 4, 0)
    control_board = np.array([[2, 6, 3, 1, 5, 4, 5, 6, 8],
                              [4, 9, 1, 5, 8, 9, 3, 4, 7],
                              [5, 8, 7, 7, 6, 3, 1, 2, 9],
                              [8, 5, 6, 5, 1, 3, 4, 1, 6],
                              [7, 3, 4, 6, 4, 9, 9, 2, 3],
                              [1, 9, 2, 2, 7, 8, 5, 7, 8],
                              [4, 8, 1, 9, 1, 6, 2, 6, 4],
                              [9, 6, 5, 3, 8, 4, 7, 8, 5],
                              [3, 7, 2, 2, 7, 5, 3, 1, 9]])
    assert np.array_equal(generator.pydoku.raw_board, control_board)


def test_handle_row_swap(generator):
    generator.pydoku.raw_board = np.array([[2, 6, 3, 1, 5, 4, 7, 9, 8],
                                           [4, 9, 1, 2, 7, 8, 3, 6, 5],
                                           [5, 8, 7, 9, 6, 3, 1, 2, 4],
                                           [8, 5, 6, 4, 3, 1, 9, 2, 7],
                                           [7, 3, 9, 6, 8, 2, 4, 1, 5],
                                           [1, 4, 2, 5, 9, 7, 3, 6, 8],
                                           [6, 1, 8, 8, 4, 6, 2, 6, 4],
                                           [9, 2, 5, 3, 1, 9, 7, 8, 5],
                                           [3, 7, 4, 7, 2, 5, 3, 1, 9]])
    generator.handle_row_swap(6, 3, 8)
    control_board = np.array([[2, 6, 3, 1, 5, 4, 7, 9, 8],
                              [4, 9, 1, 2, 7, 8, 3, 6, 5],
                              [5, 8, 7, 9, 6, 3, 1, 2, 4],
                              [8, 5, 6, 4, 3, 1, 9, 2, 7],
                              [7, 3, 9, 6, 8, 2, 4, 1, 5],
                              [1, 4, 2, 5, 9, 7, 3, 6, 8],
                              [6, 1, 5, 8, 4, 6, 2, 6, 4],
                              [9, 2, 8, 3, 1, 9, 7, 8, 5],
                              [3, 7, 4, 7, 2, 5, 3, 1, 9]])
    assert np.array_equal(generator.pydoku.raw_board, control_board)


def test_handle_col_swap(generator):
    generator.pydoku.raw_board = np.array([[2, 6, 3, 1, 5, 4, 7, 9, 8],
                                           [4, 9, 1, 2, 8, 7, 3, 6, 5],
                                           [5, 8, 7, 9, 6, 3, 1, 2, 4],
                                           [8, 5, 6, 4, 1, 3, 9, 2, 7],
                                           [7, 3, 9, 6, 2, 8, 4, 1, 5],
                                           [1, 4, 2, 5, 7, 9, 3, 6, 8],
                                           [6, 1, 8, 8, 4, 6, 2, 6, 4],
                                           [9, 2, 5, 3, 9, 1, 7, 8, 5],
                                           [3, 7, 4, 7, 2, 5, 3, 1, 9]])
    generator.handle_col_swap(8, 4, 2)
    control_board = np.array([[2, 6, 3, 1, 5, 4, 7, 9, 8],
                              [4, 9, 1, 2, 7, 8, 3, 6, 5],
                              [5, 8, 7, 9, 6, 3, 1, 2, 4],
                              [8, 5, 6, 4, 3, 1, 9, 2, 7],
                              [7, 3, 9, 6, 8, 2, 4, 1, 5],
                              [1, 4, 2, 5, 9, 7, 3, 6, 8],
                              [6, 1, 8, 8, 4, 6, 2, 6, 4],
                              [9, 2, 5, 3, 1, 9, 7, 8, 5],
                              [3, 7, 4, 7, 2, 5, 3, 1, 9]])
    assert np.array_equal(generator.pydoku.raw_board, control_board)


def test_iterate_rows(generator):
    generator.pydoku.raw_board = np.array(TEST_BOARD)
    generator.iterate_rows(0)
    assert np.array_equal(
        generator.pydoku.raw_board[:3, :], np.array([[2, 6, 3, 1, 5, 4, 7, 9, 8],
                                                     [4, 9, 1, 2, 8, 9, 3, 4, 5],
                                                     [5, 8, 7, 7, 6, 3, 1, 2, 6]]))


def test_iterate_cols(generator):
    generator.pydoku.raw_board = np.array(TEST_BOARD)
    generator.iterate_cols(0)
    assert np.array_equal(
        generator.pydoku.raw_board[:, :1], np.array([[2], [4], [5], [8], [7], [1], [6], [9], [3]]))
