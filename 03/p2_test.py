import unittest
from p2 import Solution


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.data = iter([
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ])

    def test_compute_oxygen(self):
        self.assertEqual(Solution().compute_oxygen(self.data), "10111")

    def test_compute_co2(self):
        self.assertEqual(Solution().compute_co2(self.data), "01010")

    def test_given(self):
        self.assertEqual(Solution().solve(self.data), 230)


if __name__ == "__main__":
    unittest.main()
