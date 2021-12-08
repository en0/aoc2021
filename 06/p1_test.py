from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution
from collections import deque


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = "sample.txt"
    given = 5934

    def test_1_cycle(self):
        gen = self.get_parsed_data()
        solution = Solution()
        solution.fish = deque(gen)
        solution.cycle()
        self.assertListEqual(list(solution.fish), [2, 3, 2, 0, 1])

    def test_18_cycle(self):
        gen = self.get_parsed_data()
        solution = Solution()
        solution.fish = deque(gen)
        all_expected = [
            [2, 3, 2, 0, 1],
            [1, 2, 1, 6, 0, 8],
            [0, 1, 0, 5, 6, 7, 8],
            [6, 0, 6, 4, 5, 6, 7, 8, 8],
            [5, 6, 5, 3, 4, 5, 6, 7, 7, 8],
            [4, 5, 4, 2, 3, 4, 5, 6, 6, 7],
            [3, 4, 3, 1, 2, 3, 4, 5, 5, 6],
            [2, 3, 2, 0, 1, 2, 3, 4, 4, 5],
            [1, 2, 1, 6, 0, 1, 2, 3, 3, 4, 8],
            [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 7, 8],
            [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 7, 8, 8, 8],
            [5, 6, 5, 3, 4, 5, 6, 0, 0, 1, 5, 6, 7, 7, 7, 8, 8],
            [4, 5, 4, 2, 3, 4, 5, 6, 6, 0, 4, 5, 6, 6, 6, 7, 7, 8, 8],
            [3, 4, 3, 1, 2, 3, 4, 5, 5, 6, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8],
            [2, 3, 2, 0, 1, 2, 3, 4, 4, 5, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7],
            [1, 2, 1, 6, 0, 1, 2, 3, 3, 4, 1, 2, 3, 3, 3, 4, 4, 5, 5, 6, 8],
            [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 0, 1, 2, 2, 2, 3, 3, 4, 4, 5, 7, 8],
            [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8],
        ]
        for day, expected in enumerate(all_expected):
            solution.cycle()
            self.assertListEqual(list(solution.fish), expected, f"OOPS! Wrong on day: {day+1}")


if __name__ == "__main__":
    main()
