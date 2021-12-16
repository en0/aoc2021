import heapq
import math
from typing import Iterable, Tuple
from aocfw import SolutionBase, IParser, IntMapParser
from aocfw.adt import IntVector2, IGraph, AdjacencyList
from dataclasses import dataclass


@dataclass
class Tile:

    h_cost: int
    g_cost: int = math.inf

    @property
    def f_cost(self):
        return self.g_cost + self.h_cost

    def __repr__(self):
        return str(self.h_cost)


class Solution(SolutionBase):
    bindings = {IParser: IntMapParser, IGraph: AdjacencyList}

    def neighbors(self, point: IntVector2):
        x, y = point
        points = [
                        (x+0, y-1),
            (x-1, y+0),             (x+1, y+0),
                        (x+0, y+1),
        ]
        return [(p, self.matrix[p]) for p in points if p in self.matrix]

    def find_best_cost(self, start: IntVector2, target: IntVector2):
        self.matrix[start].g_cost = 0
        _open = [(self.matrix[start].f_cost, start, [start])]
        _open_set = {start}
        _closed = set()
        while _open:
            c_f_cost, c_point, pathing = heapq.heappop(_open)
            _open_set.remove(c_point)
            c_obj = self.matrix[c_point]
            _closed.add(c_point)
            if c_point == target:
                return sum([self.matrix[p].h_cost for p in pathing]) - self.matrix[start].h_cost
            for n_point, n_obj in self.neighbors(c_point):
                new_g_cost = c_obj.f_cost
                if new_g_cost < n_obj.g_cost:
                    n_obj.g_cost = new_g_cost
                if n_point in _closed:
                    continue
                if n_point in _open_set:
                    continue
                n_pathing = pathing.copy()
                heapq.heappush(_open, (n_obj.f_cost, n_point, n_pathing + [n_point]))
                _open_set.add(n_point)

    def load(self, data: Iterable[Tuple[IntVector2, int]]) -> int:
        data = list(data)
        self.matrix = {(x, y): Tile(h_cost=v) for (x, y), v in data}
        self.start = data[0][0]
        self.end = data[-1][0]

    def solve(self, data: Iterable[Tuple[IntVector2, int]]) -> int:
        self.load(data)
        return self.find_best_cost(self.start, self.end)

    def __init__(self):
        self.matrix = {}
        self.start = None
        self.end = None


if __name__ == '__main__':
    Solution.run(source='input.txt')
