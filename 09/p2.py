from typing import Iterable
from collections import deque
from aocfw import SolutionBase, IParser
from p1 import Graph
from functools import reduce

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
                c = (x, y)
                l = (x-1, y)
                u = (x, y-1)

                # To clever? Nope, perfect amount of clever!
                if l in graph and graph.get_value(l) < 9 and graph.get_value(c) < 9:
                    graph.add_edge(c, l)
                if u in graph and graph.get_value(u) < 9 and graph.get_value(c) < 9:
                    graph.add_edge(c, u)

        yield graph


class Solution(SolutionBase):
    bindings = {IParser: GraphParser}

    def solve(self, data: Iterable[Graph]) -> int:

        basins = []
        graph: Graph = next(data)
        visited = set()

        for vertex in graph:
            size = 0
            queue = deque([vertex])
            while queue:
                _vertex = queue.popleft()
                if _vertex in visited:
                    continue
                visited.add(_vertex)
                size += 1
                for _v in graph.get_neighbors(_vertex):
                    queue.append(_v)
            if size > 1:
                basins.append(size)

        return reduce(lambda a, b: a * b, sorted(basins, reverse=True)[:3])


if __name__ == '__main__':
    Solution.run(source='input.txt')
