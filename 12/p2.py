from typing import Iterable, List, Dict, Deque, Tuple
from aocfw import SolutionBase
from p1 import Solution as _Solution
from collections import deque


class Solution(_Solution):

    def find_routes(self) -> Iterable[str]:
        small_caves = [x for x in self._graph if x.lower() == x]
        small_cave_limits = {x: 1 for x in small_caves}
        routes = set()

        for s in small_caves:
            if s in ("end", "start"):
                continue
            limits = small_cave_limits.copy()
            limits[s] = 0
            for route in self.find_routes_with_limits(limits):
                routes.add(route)

        return iter(routes)

    def find_routes_with_limits(self, visit_limits) -> Iterable[str]:
        q: Deque[Tuple[str, List[str], Dict[str]]] = deque([("start", ["start"], visit_limits)])
        while q:
            node, path, visited = q.pop()
            if node == "end":
                yield ",".join(path)
                continue
            if node in visited and visited[node] == 2:
                continue
            if node == node.lower():
                visited[node] += 1
            for _node in self._graph.neighbors(node):
                q.append((_node, path.copy() + [_node], visited.copy()))


if __name__ == '__main__':
    Solution.run(source='input.txt')
