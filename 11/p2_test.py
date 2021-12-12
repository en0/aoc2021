from unittest import TestCase, main
from aocfw import TestCaseMixin
from io import StringIO
from typing import List
from p2 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 195

    def using_sample(self, sample: List[str]):
        self.source = None
        self.sample = StringIO("\n".join(sample))

    def test_cycle_1(self):
        self.using_sample([
            "00000",
            "00000",
            "00000",
            "00000",
            "00000",
        ])
        graph = next(self.get_parsed_data())
        self.assertTrue(graph.is_all_zero())


if __name__ == '__main__':
    main()
