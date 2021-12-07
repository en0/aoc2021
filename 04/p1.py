from typing import Iterable, List
from aocfw import SolutionBase, IParser
from bingo import BingoBoard, BingoParser


class Solution(SolutionBase):
    bindings = {IParser: BingoParser}
    def solve(self, data: Iterable[any]) -> int:
        called: List[int] = next(data)
        boards: List[BingoBoard] = next(data)

        for val in called:
            for board in boards:
                if board.mark(val):
                    return board.get_score()*val
        return None


if __name__ == "__main__":
    Solution.run(source="input.txt")
