from typing import Iterable
from p1 import Solution as _Solution, Graph


class Solution(_Solution):
    def solve(self, data: Iterable[Graph]) -> int:
        counter = 0
        graph = next(data)
        while not graph.is_all_zero():
            counter += 1
            self.cycle(graph)
        return counter


if __name__ == '__main__':
    Solution.run(source='input.txt')
