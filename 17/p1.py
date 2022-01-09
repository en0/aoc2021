from typing import Iterable
from aocfw import SolutionBase, IParser, StringParser
import math


class Solution(SolutionBase):
    bindings = {IParser: StringParser}

    def load(self, data: Iterable[int]):
        self.target_y = min(map(int, next(data).split("=")[-1].split("..")))

    def triangle_number(self, n):
        return (n*(n+1))//2

    def solve(self, data: Iterable[int]) -> int:
        self.load(data)
        return self.triangle_number(abs(self.target_y + 1))


if __name__ == '__main__':
    Solution.run(source='input.txt')
