from typing import Iterable, List
from aocfw import SolutionBase
from p1 import Solution as _Solution, Operation
from functools import reduce


class GenericOperation(Operation):

    def get_value(self) -> int:
        return self._operation([f.get_value() for f in self._factors])

    def __repr__(self):
        return f'{self._sym}[{",".join(map(str, self._factors))}]'

    def __init__(self, sym: str, version: int, factors: List[Operation], operation) -> None:
        self._sym = sym
        self._factors = factors
        self._version = version
        self._operation = operation


class Solution(_Solution):

    def create_operator(self, type_id: int, version: int, factors) -> Operation:
        sym, op = {
            0: ('+', lambda f: sum(f)),
            1: ('*', lambda f: reduce(lambda a, b: a * b, f, 1)),
            2: ('min', lambda f: min(f)),
            3: ('max', lambda f: max(f)),
            5: ('gt', lambda f: 1 if f[0] > f[1] else 0),
            6: ('lt', lambda f: 1 if f[0] < f[1] else 0),
            7: ('==', lambda f: 1 if f[0] == f[1] else 0),
        }[type_id]
        return GenericOperation(sym, version, factors, op)

    def solve(self, data: Iterable[int]) -> int:
        self.load(data)
        return self.read_packet().get_value()


if __name__ == '__main__':
    Solution.run(source='input.txt')

