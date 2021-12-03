import unittest
from p1 import Solution


class SolutionTest(unittest.TestCase):
    def test_given(self):
        data = iter([
            199, 200, 208, 210,
            200, 207, 240, 269,
            260, 263,
        ])
        s = Solution()
        self.assertEqual(s.solve(data), 7)


if __name__ == "__main__":
    unittest.main()