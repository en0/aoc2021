from aocfw.typing import IParser
from typing import IO, Iterable, NamedTuple, Tuple


class Point(NamedTuple):
    x: int
    y: int


class Line:
    def is_hv(self) -> bool:
        return any([
            self.a.x == self.b.x,
            self.a.y == self.b.y,
        ])

    def __iter__(self):
        if not self.is_hv():
            raise NotImplementedError()
        for x in range(self.a.x, self.b.x + 1):
            for y in range(self.a.y, self.b.y + 1):
                yield Point(x, y)

    def _sort(self, a: Point, b: Point) -> Tuple[Point, Point]:
        ax, ay = a
        bx, by = b
        if ax == bx and ay < by:
            return Point(ax, ay), Point(bx, by)
        elif ax == bx and by < ay:
            return Point(bx, by), Point(ax, ay)
        elif ay == by and ax < bx:
            return Point(ax, ay), Point(bx, by)
        elif ay == by and bx < ax:
            return Point(bx, by), Point(ax, ay)
        else:
            return Point(*a), Point(*b)

    def __init__(self, a: Point, b: Point) -> None:
        self.a, self.b = self._sort(a, b)


class LineParser(IParser):
    def parse(self, data: IO) -> Iterable[Line]:
        for val in data:
            a, _, b = val.split(" ")
            a = tuple([int(x) for x in a.split(",")])
            b = tuple([int(x) for x in b.split(",")])
            yield Line(a, b)

