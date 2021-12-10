from typing import Iterable
from collections import deque
from aocfw import SolutionBase, IParser, StringParser


class Solution(SolutionBase):

    bindings = {IParser: StringParser}
    score_lookup = {')': 3, ']': 57, '}': 1197, '>': 25137}
    closing_lookup = {'(': ')', '[': ']', '{': '}', '<': '>'}

    def compute_line_score(self, line: str) -> int:
        q = deque()
        for s in line:
            if s in self.closing_lookup:
                q.append(self.closing_lookup[s])
            elif s != q.pop():
                return self.score_lookup[s]
        return 0

    def solve(self, data: Iterable[int]) -> int:
        return sum(map(self.compute_line_score, data))



if __name__ == '__main__':
    Solution.run(source='input.txt')
