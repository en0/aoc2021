from typing import Iterable

from p1 import Solution as _Solution


class Solution(_Solution):

    def compute_oxygen(self, data):
        data = list(data)
        gama, _ = self.compute_gama_epsilon(data)
        for i, _ in enumerate(data[0]):
            next_data = []
            for val in data:
                if val[i] == gama[i]:
                    next_data.append(val)
            data = next_data
            if len(data) == 1:
                return data[0]
            gama, _ = self.compute_gama_epsilon(data)
        return data[0]

    def compute_co2(self, data):
        data = list(data)
        _, epsilon = self.compute_gama_epsilon(data)
        for i, _ in enumerate(data[0]):
            next_data = []
            for val in data:
                if val[i] == epsilon[i]:
                    next_data.append(val)
            data = next_data
            if len(data) == 1:
                return data[0]
            _, epsilon = self.compute_gama_epsilon(data)
        return data[0]

    def solve(self, data: Iterable[int]) -> int:
        data = list(data)
        oxygen = self.compute_oxygen(data)
        co2 = self.compute_co2(data)
        return int(oxygen, base=2) * int(co2, base=2)


if __name__ == "__main__":
    Solution.run(source="input.txt")
