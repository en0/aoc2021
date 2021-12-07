from typing import Iterable, Deque
from aocfw import SolutionBase, OneLineIntegerParser, IParser
from collections import deque


class Solution(SolutionBase):
    bindings = {IParser: OneLineIntegerParser}
    fish: Deque[int] = None

    def cycle(self):
        for i, val in enumerate(list(self.fish)):
            if val == 0:
                self.fish[i] = 6
                self.fish.append(8)
            else:
                self.fish[i] = val - 1

    def solve(self, data: Iterable[int]) -> int:
        self.fish = deque(data)
        for _ in range(80):
            self.cycle()
        return len(self.fish)


if __name__ == "__main__":
    Solution.run(source="input.txt")
