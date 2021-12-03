import unittest
from p2 import Solution


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.data = iter([
            ("forward", 5),
            ("down", 5),
            ("forward", 8),
            ("up", 3),
            ("down", 8),
            ("forward", 2),
        ])

    def test_given(self):
        self.assertEqual(Solution().solve(self.data), 900)


if __name__ == "__main__":
    unittest.main()
