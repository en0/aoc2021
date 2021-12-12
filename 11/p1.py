from typing import Iterable, IO, Tuple, List, Union, NamedTuple
from functools import reduce
from collections import deque
from aocfw import SolutionBase, IParser, StringParser


class Point(NamedTuple):
    x: int
    y: int


class Graph:

    def is_all_zero(self):
        for val in self._nodes.values():
            if val != 0:
                return False
        return True

    def add(self, point: Union[Point, Tuple[int, int]], value: int):
        self._nodes[Point(*point)] = value

    def set_value(self, point: Union[Point, Tuple[int, int]], value: int):
        self.add(point, value)

    def get_value(self, point: Union[Point, Tuple[int, int]]) -> int:
        return self._nodes[point]

    def get_neighbors(self, point: Union[Point, Tuple[int, int]]) -> List[Point]:
        x, y = point
        ret = [
            Point(x-1, y-1), Point(x, y-1), Point(x+1, y-1),
            Point(x-1, y+0),                Point(x+1, y+0),
            Point(x-1, y+1), Point(x, y+1), Point(x+1, y+1),
        ]
        return [p for p in ret if p in self._nodes]

    def __repr__(self) -> str:
        mx, my = reduce(lambda a, b: (max(a[0], b[0]), max(a[1], b[1])), self._nodes.keys(), (0, 0))
        ret = []
        for y in range(my + 1):
            ret.append(" ".join([f"{self.get_value((x, y)):02}" for x in range(mx + 1)]))
        return "\n".join(ret)

    def __iter__(self):
        return iter(self._nodes.keys())

    def __init__(self):
        self._nodes = {}


class GraphParser(StringParser):

    def parse(self, data: IO) -> Iterable[Graph]:
        for y, line in enumerate(super().parse(data)):
            for x, val in enumerate(line):
                self._graph.add((x, y), int(val))
        yield self._graph

    def __init__(self, graph: Graph):
        self._graph = graph


class Solution(SolutionBase):
    bindings = {
        IParser: GraphParser,
        Graph: Graph,
    }

    def cycle(self, graph: Graph):
        has_flashed = set()
        flashes = 0
        q = deque(list(graph))
        while q:
            point = q.pop()
            if point in has_flashed:
                continue
            val = graph.get_value(point)
            if val == 9:
                flashes += 1
                has_flashed.add(point)
                graph.set_value(point, 0)
                for _point in graph.get_neighbors(point):
                    q.append(_point)
            else:
                graph.set_value(point, val + 1)
        return flashes

    def solve(self, data: Iterable[Graph]) -> int:
        graph = next(data)
        return sum([self.cycle(graph) for _ in range(100)])


if __name__ == '__main__':
    Solution.run(source='input.txt')
