from typing import Iterable
from aocfw import SolutionBase, OneLineIntegerParser, IParser


class Solution(SolutionBase):
    bindings = {IParser: OneLineIntegerParser}

    def get_target(self, data: Iterable[int]):
        data = list(sorted(data))
        return data[len(data) // 2]

    def get_fuel_cost(self, data: Iterable[int], target: int):
        return sum(map(lambda x: abs(x - target), data))

    def solve(self, data: Iterable[int]) -> int:
        data = list(data)
        target = self.get_target(data)
        return self.get_fuel_cost(data, target)


if __name__ == "__main__":
    Solution.run(source="input.txt")
