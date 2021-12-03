import unittest
from p1 import Solution


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.data = iter([
        ])

    unittest.skip("n/a")
    def test_given(self):
        expected = None
        self.assertEqual(Solution().solve(self.data), expected)


if __name__ == "__main__":
    unittest.main()
