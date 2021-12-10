from typing import Iterable, Optional
from collections import deque
from aocfw import SolutionBase, IParser, StringParser
from functools import reduce


class Solution(SolutionBase):

    bindings = {IParser: StringParser}
    score_lookup = {')': 1, ']': 2, '}': 3, '>': 4}
    closing_lookup = {'(': ')', '[': ']', '{': '}', '<': '>'}

    def get_score(self, s: str):
        return reduce(lambda a, b: a * 5 + self.score_lookup[b], s, 0)

    def find_closing_string(self, line: str) -> Optional[str]:
        q = deque()
        for s in line:
            if s in self.closing_lookup:
                q.append(self.closing_lookup[s])
            elif s != q.pop():
                return None
        return "".join(reversed(q))

    def solve(self, data: Iterable[int]) -> int:
        scores = []
        for line in data:
            if ending := self.find_closing_string(line):
                scores.append(self.get_score(ending))
        return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
    Solution.run(source='input.txt')
