from typing import Iterable
from aocfw import SolutionBase


class Solution(SolutionBase):
    def solve(self, data: Iterable[int]) -> int:
        count = 0
        last = next(data)
        for val in data:
            if val > last:
                count += 1
            last = val
        return count


if __name__ == "__main__":
    Solution.run(source="input.txt")
