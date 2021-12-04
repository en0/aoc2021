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

    def test_compute_gama_epsilon(self):
        gama, epsilon = Solution().compute_gama_epsilon(self.data)
        self.assertEqual(gama, '10110')
        self.assertEqual(epsilon, '01001')

    def test_given(self):
        self.assertEqual(Solution().solve(self.data), 198)


if __name__ == "__main__":
    unittest.main()
