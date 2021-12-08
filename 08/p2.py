from typing import Iterable
from aocfw import SolutionBase, IParser


class BetterSegmentOutputParser(IParser):
    def parse(self, data):
        for line in data:
            i, o = line.rstrip("\n").split(" | ")
            yield tuple(map(set, i.split(" "))), tuple(map(set, o.split(" ")))


class Solution(SolutionBase):
    bindings = {IParser: BetterSegmentOutputParser}

    def set_to_str(self, val):
        return "".join(sorted(val))

    def collect_by_count(self, data):
        ret = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
        for val in data:
            ret[len(val)].append(val)
        return ret

    def select(self, data, predicate = None):
        predicate = predicate or (lambda x: True)
        return [x for x in data if predicate(x)][0]

    def map_values(self, data):
        ret = {}
        by_count = self.collect_by_count(data)
        ret[1] = self.select(by_count[2])
        ret[4] = self.select(by_count[4])
        ret[7] = self.select(by_count[3])
        ret[8] = self.select(by_count[7])
        ret[3] = self.select(by_count[5], lambda x: len(ret[1] - x) == 0)
        ret[9] = ret[4] | ret[3]
        ret[6] = self.select(by_count[6], lambda x: len(x - ret[1]) == 5)
        ret[0] = self.select(by_count[6], lambda x: x not in (ret[9], ret[6]))
        ret[5] = self.select(by_count[5], lambda x: len(x - ret[6]) == 0)
        ret[2] = self.select(by_count[5], lambda x: x not in (ret[3], ret[5]))
        return {self.set_to_str(v): str(k) for k, v in ret.items()}

    def decode_value(self, mapping, outputs):
        digs = []
        for val in map(self.set_to_str, outputs):
            digs.append(mapping[val])
        return int("".join(digs))

    def solve(self, data: Iterable[int]) -> int:
        return sum([self.decode_value(self.map_values(i), o) for i, o in data])


if __name__ == '__main__':
    Solution.run(source='input.txt')

