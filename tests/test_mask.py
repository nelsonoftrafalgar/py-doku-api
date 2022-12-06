import pytest
from py_doku.src.mask import Mask


@pytest.fixture
def mask():
    return Mask()


def test_mask_board(mask):
    masked_board = mask.mask_board(0.7)
    expected = [all(row) for row in masked_board]
    assert not any(expected)
