import math
from typing import Iterable, Tuple
from aocfw import SolutionBase, IParser, OneLineIntegerParser


class Solution(SolutionBase):
    bindings = {IParser: OneLineIntegerParser}

    def get_triangular_number(self, val: int) -> int:
        ret = (val + 1) * (val // 2)
        return ret if val % 2 == 0 else ret + (val // 2) + 1

    def get_target(self, data: Iterable[int]) -> Tuple[int, int]:
        data = list(data)
        return (
            math.floor(sum(data) / len(data)),
            math.ceil(sum(data) / len(data))
        )

    def get_fuel_cost(self, data: Iterable[int], target: int) -> int:
        return sum(map(lambda x: self.get_triangular_number(abs(x - target)), data))

    def solve(self, data: Iterable[int]) -> int:
        data = list(data)
        low, high = self.get_target(data)
        return min([
            self.get_fuel_cost(data, low),
            self.get_fuel_cost(data, high)
        ])


if __name__ == "__main__":
    Solution.run(source="input.txt")
