EMPTY = ""


class Board:
    def __init__(self, width: int = 7, height: int = 5):
        self.columns: list[list] = [[] for _ in range(width)]
        self.width = width
        self.height = height

    def play(self, column_index: int, player: str):
        if (
            column_index < 0
            or column_index >= self.width
            or (len((column := self.columns[column_index])) >= self.height)
        ):
            raise IndexError

        column.append(player)

    def __getitem__(self, index: tuple[int, int]):
        column = self.columns[index[0]]
        if len(column) <= index[1]:
            return EMPTY
        return column[index[1]]
