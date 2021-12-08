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

    def map_values(self, data):
        ret = {}
        by_count = self.collect_by_count(data)
        ret[1] = by_count[2][0]
        ret[4] = by_count[4][0]
        ret[7] = by_count[3][0]
        ret[8] = by_count[7][0]
        ret[3] = [x for x in by_count[5] if len(ret[1] - x) == 0][0]
        ret[9] = ret[4] | ret[3]
        ret[6] = [x for x in by_count[6] if len(x - ret[1]) == 5][0]
        ret[0] = [x for x in by_count[6] if x not in [ret[9], ret[6]]][0]
        ret[5] = [x for x in by_count[5] if len(x - ret[6]) == 0][0]
        ret[2] = [x for x in by_count[5] if x not in (ret[3], ret[5])][0]
        return {self.set_to_str(v): str(k) for k, v in ret.items()}

    def decode_value(self, mapping, outputs):
        digs = []
        for val in map(self.set_to_str, outputs):
            digs.append(mapping[val])
        return int("".join(digs))

    def solve(self, data: Iterable[int]) -> int:
        return sum([
            self.decode_value(self.map_values(_in), _out)
            for _in, _out in data
        ])


if __name__ == '__main__':
    Solution.run(source='input.txt')

