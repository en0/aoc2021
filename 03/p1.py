from typing import Iterable
from aocfw import SolutionBase, StringParser, IParser


class Solution(SolutionBase):

    bindings = {
        IParser: StringParser
    }

    def compute_gama_epsilon(self, data):
        ones, total = None, 0
        for val in data:
            ones = [0] * len(val) if not ones else ones
            total += 1
            for i, v in enumerate(val):
                ones[i] += int(v)
        return (
            "".join(["1" if v >= (total / 2) else "0" for v in ones]),
            "".join(["0" if v >= (total / 2) else "1" for v in ones]),
        )

    def solve(self, data: Iterable[str]) -> int:
        gama, epsilon = self.compute_gama_epsilon(data)
        return int(gama, base=2) * int(epsilon, base=2)


if __name__ == "__main__":
    Solution.run(source="input.txt")
