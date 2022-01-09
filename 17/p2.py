from typing import Iterable
from aocfw import SolutionBase


class Solution(SolutionBase):
    def solve(self, data: Iterable[int]) -> int:
        #x=24
        #y=56
        x=10
        y=5

        rt = 0
        for i in range(min(x, y)):
            rt += (x-i) * (y-i)
        print(rt)



if __name__ == '__main__':
    Solution.run(source='input.txt')
