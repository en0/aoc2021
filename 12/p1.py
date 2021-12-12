from typing import Iterable, Deque, Set, Tuple, List
from aocfw import SolutionBase, IParser, StringParser
from aocfw.adt import IGraph, AdjacencyList
from collections import deque


class Solution(SolutionBase):
    bindings = {
        IGraph: AdjacencyList,
        IParser: StringParser,
    }

    def load(self, data):
        for line in list(data):
            x, y = line.split("-")
            if x not in self._graph:
                self._graph.add_vertex(x)
            if y not in self._graph:
                self._graph.add_vertex(y)
            self._graph.add_edge(x, y)
            self._graph.add_edge(y, x)

    def find_routes(self) -> Iterable[str]:
        # struct = [node, path, visited_small_caves]
        q: Deque[Tuple[str, List[str], Set[str]]] = deque([("start", ["start"], set())])
        while q:
            node, path, visited = q.pop()
            if node == "end":
                yield ",".join(path)
                continue
            if node in visited:
                continue
            if node == node.lower():
                visited.add(node)
            for _node in self._graph.neighbors(node):
                q.append((_node, path.copy() + [_node], visited.copy()))

    def solve(self, data: Iterable[str]) -> int:
        self.load(data)
        return sum(1 for _ in self.find_routes())

    def __init__(self, graph: IGraph):
        self._graph = graph


if __name__ == '__main__':
    Solution.run(source='input.txt')
