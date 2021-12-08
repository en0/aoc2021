from typing import Iterable, Tuple
from aocfw import SolutionBase, IParser


class SegmentOutputParser(IParser):
    def parse(self, data):
        for line in data:
            _, o = line.rstrip("\n").split(" | ")
            yield tuple(o.split(" "))


class Solution(SolutionBase):
    bindings = {IParser: SegmentOutputParser}

    def count_easy_ones(self, dat: Tuple[str, str, str, str]):
        return len([v for v in dat if len(v) in (2, 3, 4, 7)])

    def solve(self, data: Iterable[int]) -> int:
        return sum(map(self.count_easy_ones, data))


if __name__ == '__main__':
    Solution.run(source='input.txt')

