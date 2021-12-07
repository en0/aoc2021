from unittest import TestCase, main
from aocfw import TestCaseMixin
from p2 import Solution


class SolutionTest(TestCase, TestCaseMixin):

    solution = Solution
    source = "sample.txt"
    given = 230

    def test_compute_oxygen(self):
        data = self.get_parsed_data()
        self.assertEqual(Solution().compute_oxygen(data), "10111")

    def test_compute_co2(self):
        data = self.get_parsed_data()
        self.assertEqual(Solution().compute_co2(data), "01010")


if __name__ == "__main__":
    main()
