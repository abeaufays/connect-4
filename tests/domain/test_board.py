import pytest
from connect4.domain import models


class TestBoard:
    def test_play_first(self):
        board = models.Board()

        board.play(1, models.PLAYER_1)

        assert board[1, 0] == models.PLAYER_1
        assert board[0, 0] == models.EMPTY

    def test_play_illegal_moves(self):
        board = models.Board(width=7, height=5)
        for _ in range(5):
            board.play(2, models.PLAYER_1)

        with pytest.raises(IndexError):
            board.play(-1, models.PLAYER_1)
        with pytest.raises(IndexError):
            board.play(7, models.PLAYER_1)

        with pytest.raises(IndexError):
            board.play(2, models.PLAYER_1)
