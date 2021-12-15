from typing import Iterable
from aocfw import SolutionBase, IParser, StringParser
from aocfw.adt import AdjacencyList
from aocfw.adt.typing import IGraph
from functools import lru_cache
from collections import deque
from p1 import Solution as _Solution


class Solution(SolutionBase):
    bindings = {
        IParser: StringParser,
        IGraph: AdjacencyList
    }

    def load(self, data: Iterable[int]) -> int:
        self.poly = next(data)
        assert(next(data) == "")
        instructions = dict(map(lambda v: v.split(" -> "), data))
        for key in instructions.keys():
            self.graph.add_vertex(key)
        for key, value in instructions.items():
            self.graph.add_edge(key, key[0]+value)
            self.graph.set_weight(key, key[0]+value, 1)
            self.graph.add_edge(key, value+key[1])
            self.graph.set_weight(key, value+key[1], 2)

    def merge_dict_counts(self, a, b):
        ret = b.copy()
        for k, v in a.items():
            ret.setdefault(k, 0)
            ret[k] += v
        return ret

    def compute_score(self, counts) -> int:
        x = sorted(counts.values())
        return x[-1] - x[0]

    @lru_cache(maxsize=2000)
    def count_chars(self, key, depth) -> dict:
        if depth == 0:
            return {key[1]: 1}
        a, b = list(self.graph.neighbors(key))
        return self.merge_dict_counts(
            self.count_chars(a, depth-1),
            self.count_chars(b, depth-1)
        )

    def solve(self, data: Iterable[int], limit=40) -> int:
        self.load(data)
        counts = {self.poly[0]: 1}
        for i in range(0, len(self.poly)-1):
            counts = self.merge_dict_counts(counts, self.count_chars(self.poly[i:i+2], limit))
        return self.compute_score(counts)


    def __init__(self, graph: IGraph):
        self.graph = graph

if __name__ == '__main__':
    Solution.run(source='input.txt')
