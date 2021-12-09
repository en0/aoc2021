from typing import Iterable
from aocfw import SolutionBase, IParser
from typing import NamedTuple, Tuple, Dict, Set, List
from collections import deque

Point = Tuple[int, int]


class Graph:
    def add_vertex(self, ident: Point, value: int) -> None:
        self._verts[ident] = value
        self._edges.setdefault(ident, set())

    def add_edge(self, a: Point, b: Point):
        if a not in self._edges:
            return
        if b not in self._edges:
            return
        self._edges[a].add(b)
        self._edges[b].add(a)

    def get_neighbors(self, ident: Point) -> List[Point]:
        return self._edges.get(ident, set())

    def get_value(self, ident: Point) -> int:
        return self._verts[ident]

    def __iter__(self):
        return iter(self._verts.keys())

    def __contains__(self, value: Point) -> bool:
        return value in self._verts

    def __init__(self):
        self._edges: Dict[Point, Set[Point]] = {}
        self._verts: Dict[Point, int] = {}


class GraphParser(IParser):
    def parse(self, data):
        graph = Graph()
        max_x, max_y = 0, 0
        for y, line in enumerate(data):
            max_y = max(y, max_y)
            for x, val in enumerate(line.rstrip("\n")):
                max_x = max(x, max_x)
                graph.add_vertex((x, y), int(val))
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                graph.add_edge((x, y), (x-1, y))
                graph.add_edge((x, y), (x, y-1))
        yield graph



class Solution(SolutionBase):
    bindings = {IParser: GraphParser}

    def get_lower_neighbors(self, graph: Graph, vertex: Point):
        return [
            p for p in graph.get_neighbors(vertex)
            if graph.get_value(p) <= graph.get_value(vertex)
        ]

    def collect_low_points(self, graph: Graph):
        lowest_points = set()
        queue = deque([x for x in graph])
        visited = set()

        while queue:
            vertex = queue.popleft()
            if vertex in visited:
                continue
            visited.add(vertex)
            neighbors = self.get_lower_neighbors(graph, vertex)
            for d in neighbors:
                queue.append(d)
            if len(neighbors) == 0:
                lowest_points.add(vertex)
        return lowest_points

    def solve(self, data: Iterable[Graph]) -> int:
        graph: Graph = next(data)
        return sum(map(lambda x: graph.get_value(x) + 1, self.collect_low_points(graph)))


if __name__ == '__main__':
    Solution.run(source='input.txt')
