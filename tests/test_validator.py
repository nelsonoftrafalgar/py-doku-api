import pytest
import numpy as np
from py_doku.src.validator import Validator
from tests import VALID_BOARD, INVALID_BOARD


@pytest.fixture
def validator():
    return Validator()


def test_validate_sectors(validator):
    assert validator.validate_sectors(VALID_BOARD)
    assert not validator.validate_sectors(INVALID_BOARD)


def test_validate_rows(validator):
    assert validator.validate_rows(VALID_BOARD)
    assert not validator.validate_rows(INVALID_BOARD)


def test_validate_cols(validator):
    assert validator.validate_cols(VALID_BOARD)
    assert not validator.validate_cols(INVALID_BOARD)


def test_validate_board(validator):
    assert validator.validate_board(VALID_BOARD)
    assert not validator.validate_board(INVALID_BOARD)
