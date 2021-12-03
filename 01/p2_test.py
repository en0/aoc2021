import unittest
from p2 import Solution


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.data = iter([
            199, 200, 208, 210,
            200, 207, 240, 269,
            260, 263,
        ])

    def test_windowed(self):
        s = Solution()
        r = s.windowed(self.data)
        self.assertEqual(next(r), 607)
        self.assertEqual(next(r), 618)

    def test_solution(self):
        s = Solution()
        self.assertEqual(s.solve(self.data), 5)


if __name__ == "__main__":
    unittest.main()
