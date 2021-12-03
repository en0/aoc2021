import unittest
from p1 import Solution


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

    unittest.skip("n/a")
    def test_given(self):
        self.assertEqual(Solution().solve(self.data), 198)


if __name__ == "__main__":
    unittest.main()
