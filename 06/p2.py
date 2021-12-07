from typing import Iterable, Dict
from aocfw import SolutionBase, OneLineIntegerParser, IParser


class Solution(SolutionBase):
    bindings = {IParser: OneLineIntegerParser}
    fish: Dict[int, int] = None

    def load_catalog(self, fish: Iterable[int]):
        self.fish = {i: 0 for i in range(9)}
        for val in fish:
            self.fish[val] += 1

    def cycle(self):
        n_fish = {i: 0 for i in range(9)}
        for age, count in self.fish.items():
            if age == 0:
                n_fish[6] += count
                n_fish[8] += count
            else:
                n_fish[age - 1] += count
        self.fish = n_fish

    def solve(self, data: Iterable[int]) -> int:
        self.load_catalog(data)
        for _ in range(256):
            self.cycle()
        return sum(self.fish.values())


if __name__ == "__main__":
    Solution.run(source="input.txt")
