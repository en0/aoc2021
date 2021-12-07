from aocfw.typing import IParser
from typing import IO, Iterable, NamedTuple, Tuple


class Point(NamedTuple):
    x: int
    y: int


class Line:
    def is_hv(self) -> bool:
        return self._is_hv

    def __iter__(self):
        if self.is_hv():
            for x in range(self.a.x, self.b.x + 1):
                for y in range(self.a.y, self.b.y + 1):
                    yield Point(x, y)
        else:
            ax, ay = self.a
            bx, by = self.b
            x_step = 1 if ax < bx else -1
            y_step = 1 if ay < by else -1
            for x, y in zip(range(ax, bx + x_step, x_step), range(ay, by + y_step, y_step)):
                yield Point(x, y)

    def _sort(self, a: Point, b: Point) -> Tuple[Point, Point, bool]:
        ax, ay = a
        bx, by = b
        if ax == bx and ay < by:
            return Point(ax, ay), Point(bx, by), True
        elif ax == bx and by < ay:
            return Point(bx, by), Point(ax, ay), True
        elif ay == by and ax < bx:
            return Point(ax, ay), Point(bx, by), True
        elif ay == by and bx < ax:
            return Point(bx, by), Point(ax, ay), True
        else:
            return Point(*a), Point(*b), False

    def __init__(self, a: Point, b: Point) -> None:
        self.a, self.b, self._is_hv = self._sort(a, b)


class LineParser(IParser):
    def parse(self, data: IO) -> Iterable[Line]:
        for val in data:
            a, _, b = val.split(" ")
            a = tuple([int(x) for x in a.split(",")])
            b = tuple([int(x) for x in b.split(",")])
            yield Line(a, b)

