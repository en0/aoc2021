from typing import Iterable, List
from aocfw import SolutionBase, IParser, StringParser
from io import StringIO
from dataclasses import dataclass


class Hex2BinParser(IParser):
    def parse(self, data):
        result = []
        for c in next(data).rstrip("\n"):
            val = int(c, base=16)
            result.append(f"{val:04b}")
        yield "".join(result)


class Operation:

    def get_value(self) -> int:
        raise NotImplementedError()

    def sum_version(self) -> int:
        raise NotImplementedError()


class Literal(Operation):

    def get_value(self) -> int:
        return self._value

    def sum_version(self) -> int:
        return self._version

    def __repr__(self):
        return f'L{self._value}'

    def __init__(self, version: int, value: int) -> None:
        self._value = value
        self._version = version


class Operator(Operation):

    def sum_version(self) -> int:
        return sum(map(lambda x: x.sum_version(), self._factors)) + self._version

    def __repr__(self):
        return f'O[{",".join(map(str, self._factors))}]'

    def __init__(self, version: int, factors: List[Operation]) -> None:
        self._factors = factors
        self._version = version


def b2i(v):
    return int(v, base=2)


class Solution(SolutionBase):

    bindings = {IParser: Hex2BinParser}

    def load(self, data: Iterable[int]) -> int:
        self.stream = StringIO(next(data))

    def _read_literal(self) -> int:
        value_parts = []
        keep_reading = True
        while keep_reading:
            keep_reading = self.stream.read(1) == '1'
            value_parts.append(self.stream.read(4))
        return b2i("".join(value_parts))

    def _read_factors(self) -> List[Operation]:
        length_type_id = self.stream.read(1)
        factors = []
        if length_type_id == '0':
            size = b2i(self.stream.read(15))
            offset_limit = self.stream.tell() + size
            while self.stream.tell() < offset_limit:
                factors.append(self.read_packet())
        else:
            count = b2i(self.stream.read(11))
            for _ in range(count):
                factors.append(self.read_packet())
        return factors

    def read_packet(self) -> Operation:
        version = b2i(self.stream.read(3))
        type_id = b2i(self.stream.read(3))
        if type_id == 4:
            value = self._read_literal()
            return Literal(version, value)
        else:
            factors = self._read_factors()
            return self.create_operator(type_id, version, factors)

    def create_operator(self, type_id: int, version: int, factors) -> Operation:
        return Operator(version, factors)

    def solve(self, data: Iterable[int]) -> int:
        self.load(data)
        return self.read_packet().sum_version()


if __name__ == '__main__':
    Solution.run(source='input.txt')
