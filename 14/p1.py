from typing import Iterable, Dict, List, Tuple
from aocfw import SolutionBase, IParser, StringParser


class Solution(SolutionBase):

    instructions: Dict[str, str] = None
    poly: str = None
    bindings = {IParser: StringParser}

    def load(self, data: Iterable[int]) -> int:
        self.poly = next(data)
        assert(next(data) == "")
        self.instructions = dict(map(lambda v: v.split(" -> "), data))

    def do_insert_step(self):
        for i in range(len(self.poly)-2, -1, -1):
            key = self.poly[i:i+2]
            if key in self.instructions:
                self.poly = self.instructions[key].join([self.poly[:i+1], self.poly[i+1:]])

    def compute_score(self):
        char_counts = {}
        for c in self.poly:
            char_counts.setdefault(c, 0)
            char_counts[c] += 1
        x = sorted(char_counts.values())
        return x[-1] - x[0]

    def solve(self, data: Iterable[int], limit=10) -> int:
        self.load(data)
        for _ in range(limit):
            self.do_insert_step()
        return self.compute_score()


if __name__ == '__main__':
    Solution.run(source='input.txt')
