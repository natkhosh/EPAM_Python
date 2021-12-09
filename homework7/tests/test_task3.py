import pytest

from homework7.task_3.task_3 import tic_tac_toe_checker


@pytest.mark.parametrize('board, expected_result', [
    ([["x", "-", "0"], ["-", "0", "0"], ["0", "x", "x"]], '0 wins!'),
    ([["-", "-", "x"], ["-", "x", "0"], ["x", "x", "0"]], 'x wins!'),
    ([["-", "-", "0"], ["-", "x", "0"], ["x", "0", "x"]], 'unfinished!'),
    ([["0", "x", "0"], ["0", "x", "0"], ["x", "0", "x"]], 'draw!')
])
def test_tic_tac_toe_checker(board, expected_result):
    """ Testing that function checks if the are some winners. """
    assert tic_tac_toe_checker(board) == expected_result
