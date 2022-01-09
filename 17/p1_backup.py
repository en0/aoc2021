from typing import Iterable, Tuple, Optional
from aocfw import SolutionBase, IParser, StringParser
from aocfw.adt import IntVector2
from dataclasses import dataclass

@dataclass
class Boundary:

    x: Tuple[int]
    y: Tuple[int]

    def check_point(self, point: Tuple[int, int]):
        if point in self:
            return 0
        elif self.y[1] < point[1] and self.x[1] > point[0]:
            return -1
        elif self.x[0] > point[0] and self.y[0] < point[1]:
            return -1
        return 1

    def __contains__(self, point: Tuple[int, int]):
        return self.x[0] <= point[0] <= self.x[1] and self.y[1] >= point[1] >= self.y[0]


class Solution(SolutionBase):
    bindings = {IParser: StringParser}

    def load(self, data: Iterable[int]):
        """target area: x=235..259, y=-118..-62"""
        _, vals = next(data).split(": ")
        x, y = [[int(_v) for _v in v[2:].split("..")] for v in vals.split(", ")]
        self.boundary = Boundary(tuple(sorted(x)), tuple(sorted(y)))

    def shoot_prob(self, vector: Tuple[int, int]) -> Optional[int]:
        c = IntVector2(0, 0)
        h = 0
        vector = IntVector2(*vector)
        drag = IntVector2(-1, 0)
        gravity = IntVector2(0, -1)

        while True:
            c += vector
            ck = self.boundary.check_point(c)
            h = max(h, c.y)
            if ck == 0:
                print(c)
                return h
            elif ck > 0:
                print(c)
                return None
            vector += gravity
            if vector.x > 0:
                vector += drag
            elif vector.x < 0:
                vector -= drag

        if c in self.boundary:
            return 1

    def solve(self, data: Iterable[int]) -> int:
        self.load(data)
        return self.shoot_prob((22, 117))


if __name__ == '__main__':
    Solution.run(source='input.txt')
