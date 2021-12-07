from unittest import TestCase, main
from aocfw import TestCaseMixin
from p2 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = "sample.txt"
    given = 12

    def test_iter_points(self):
        data = self.get_parsed_data()

        line = list(next(data))
        all_expected = [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]
        self.assertEqual(len(line), len(all_expected))
        for expected, actual in zip(all_expected, line):
            self.assertEqual(expected, actual)

        line = list(next(data))
        all_expected = [(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)]
        self.assertEqual(len(line), len(all_expected))
        for expected, actual in zip(all_expected, line):
            self.assertEqual(expected, actual)

        line = list(next(data))
        all_expected = [(3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4)]
        self.assertEqual(len(line), len(all_expected))
        for expected, actual in zip(all_expected, line):
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
