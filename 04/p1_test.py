import unittest
from io import StringIO
from p1 import Solution


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.data = iter([
        ])

    @unittest.skip("n/a")
    def test_given(self):
        self.assertEqual(Solution().solve(self.data), 4512)


if __name__ == "__main__":
    unittest.main()
