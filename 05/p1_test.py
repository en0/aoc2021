from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution
from parser import Line


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = "sample.txt"
    given = 5

    def test_paser(self):
        gen = self.get_parsed_data()
        line = next(gen)
        self.assertIsInstance(line, Line)

    def test_line_hv(self):
        for expected, line in zip([True, False], self.get_parsed_data()):
            self.assertEqual(expected, line.is_hv())

    def test_iter_points(self):
        data = self.get_parsed_data()

        line = list(next(data))
        all_expected = [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]
        self.assertEqual(len(line), len(all_expected))
        for expected, actual in zip(all_expected, line):
            self.assertEqual(expected, actual)

        # Skip this one, its not "hv"
        next(data)

        line = list(next(data))
        all_expected = [(3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4)]
        self.assertEqual(len(line), len(all_expected))
        for expected, actual in zip(all_expected, line):
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
