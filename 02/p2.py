from typing import Iterable
from aocfw import SolutionBase
from aocfw.typing import IParser

from parser import SubmarineInstructionParser


class Solution(SolutionBase):
    bindings = {
        IParser: SubmarineInstructionParser
    }

    def solve(self, data: Iterable[int]) -> int:
        x, z, aim = 0, 0, 0
        for inst, val in data:
            if inst == "forward":
                x += val
                z += val * aim
            if inst == "down":
                aim += val
            if inst == "up":
                aim -= val
        return x * z


if __name__ == "__main__":
    Solution.run(source="input.txt")
