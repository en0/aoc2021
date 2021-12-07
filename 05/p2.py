from typing import Iterable
from aocfw import SolutionBase, IParser

from parser import LineParser


class Solution(SolutionBase):

    bindings = {
        IParser: LineParser
    }

    def solve(self, data: Iterable[int]) -> int:
        counter = {}
        for line in data:
            for point in line:
                counter.setdefault(point, 0)
                counter[point] += 1
        return len([x for x in counter.values() if x > 1])


if __name__ == "__main__":
    Solution.run(source="input.txt")
