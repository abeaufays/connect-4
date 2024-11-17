import pytest
from connect4.domain import boards


class TestBoard:
    def test_play_first(self):
        board = boards.Board()

        board.play(1, "X")

        assert board[1, 0] == "X"
        assert board[0, 0] == boards.EMPTY
        assert (
            sum(
                board[column, row] != boards.EMPTY
                for row in range(board.height)
                for column in range(board.width)
            )
            == 1
        )

    def test_play_illegal_moves(self):
        board = boards.Board(width=7, height=5)
        for _ in range(5):
            board.play(2, "X")

        with pytest.raises(IndexError):
            board.play(-1, "X")
        with pytest.raises(IndexError):
            board.play(7, "X")

        with pytest.raises(IndexError):
            board.play(2, "X")
