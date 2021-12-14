from typing import Iterable
from aocfw import SolutionBase, IParser, StringParser
from functools import partial
import numpy as np


class Solution(SolutionBase):
    bindings = {IParser: StringParser}

    def load_matrix(self, data: Iterable[str]):
        coords = []
        x_max, y_max = 0, 0
        for coord in data:
            if coord == "":
                break
            x, y = [int(_) for _ in coord.split(",")]
            x_max = max(x_max, x)
            y_max = max(y_max, y)
            coords.append((x, y))
        self.matrix = np.zeros((y_max+1, x_max+1), dtype=int)
        for x, y in coords:
            # NumPy wants y axis first since it's the index into the "rows".
            self.matrix[y, x] = 1

    def load_fold_instructions(self, data: Iterable[str]):
        for instruction in data:
            axis, at = instruction.split("=")
            self.instructions.append(
                partial(self.fold_x, int(at))
                if axis.endswith("x")
                else partial(self.fold_y, int(at))
            )

    def load(self, data: Iterable[str]):
        self.load_matrix(data)
        self.load_fold_instructions(data)

    def fold_x(self, value: int):
        """np.fliplr(self.matrix)"""
        left = self.matrix[:, 0:value]
        right = np.fliplr(self.matrix[:, value+1:])
        self.matrix = np.add(left, right)

    def fold_y(self, value: int):
        """np.flipud(self.matrix)"""
        top = self.matrix[0:value, :]
        bot = np.flipud(self.matrix[value + 1:, :])
        self.matrix = np.add(top, bot)

    def solve(self, data: Iterable[str]) -> int:
        self.load(data)
        self.instructions[0]()
        return np.count_nonzero(self.matrix)

    def __init__(self):
        self.matrix = []
        self.instructions = []


if __name__ == '__main__':
    Solution.run(source='input.txt')
