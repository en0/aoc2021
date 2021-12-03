from typing import Iterable
from p1 import Solution as _Solution
from collections import deque


class Solution(_Solution):

    def windowed(self, data):
        a, b, c, *data = data
        d = deque([a, b, c], maxlen=3)
        for val in data:
            yield sum(d)
            d.append(val)
        yield sum(d)

    def solve(self, data: Iterable[int]) -> int:
        data = self.windowed(data)
        return super().solve(data)


if __name__ == "__main__":
    Solution.run(source="input.txt")
