from typing import IO, Iterable

from aocfw.typing import IParser


class BingoBoard:

    def append(self, row: Iterable[int]):
        for v in row:
            self._set.add(v)
            self._numbers.append(v)
            self._marks.append(False)

    def check_board(self):
        for i in range(5):
            if all(self._marks[(i*5):(i*5)+5]):
                return True
            elif all([
                self._marks[i],
                self._marks[i+5],
                self._marks[i+10],
                self._marks[i+15],
                self._marks[i+20],
            ]):
                return True
        return False

    def mark(self, value) -> bool:
        if value not in self._set:
            return False
        for i, v in enumerate(self._numbers):
            if v == value:
                self._marks[i] = True
        return self.check_board()

    def __init__(self):
        self._set = set()
        self._numbers = []
        self._marks = []


class BingoParser(IParser):
    def parse(self, data: IO) -> Iterable[any]:
        yield map(int, next(data).split(","))
        boards = []
        for line in map(lambda x: x.rstrip("\n"), data):
            if line == "":
                board = BingoBoard()
                boards.append(board)
            else:
                board.append([int(x) for x in line.split(" ") if x != ""])
        yield boards
