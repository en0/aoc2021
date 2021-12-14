from typing import Iterable
from aocfw import SolutionBase
from p1 import Solution as _Solution
import numpy as np


class Solution(_Solution):

    def print_matrix(self):
        for row in self.matrix:
            row_out = []
            for cell in row:
                row_out.append("*" if cell != 0 else " ")
            print("".join(row_out))

    def solve(self, data: Iterable[str]) -> int:
        self.load(data)
        for instruction in self.instructions:
            instruction()
        self.print_matrix()
        return "See output"


if __name__ == '__main__':
    Solution.run(source='input.txt')
