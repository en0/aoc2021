from typing import Iterable, Deque
from aocfw import SolutionBase
from aocfw.typing import IParser
from collections import deque
from bingo import BingoParser, BingoBoard


class Solution(SolutionBase):
    bindings = {IParser: BingoParser}

    def solve(self, data: Iterable[any]) -> int:

        called: List[int] = next(data)
        boards: Deque[BingoBoard] = deque(next(data))

        last_board = None
        last_value = None
        for val in called:
            for board in list(boards):
                if board.mark(val):
                    boards.remove(board)
                    last_board, last_value = board, val

        return last_board.get_score()*last_value


if __name__ == "__main__":
    Solution.run(source="input.txt")
