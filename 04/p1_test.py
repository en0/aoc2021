from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution

from bingo import BingoBoard


class SolutionTest(TestCase, TestCaseMixin):

    solution = Solution
    source = "sample.txt"
    given = 4512

    def test_boards_are_boards(self):
        gen = self.get_parsed_data()
        next(gen)
        boards = list(next(gen))
        self.assertEqual(len(boards), 3)
        for board in boards:
            self.assertIsInstance(board, BingoBoard)


    def test_called_numbers(self):
        gen = self.get_parsed_data()
        self.assertListEqual(list(next(gen)), [
            7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21,
            24, 10, 16, 13, 6, 15, 25, 12, 22, 18,
            20, 8, 19, 3, 26, 1
        ])


if __name__ == "__main__":
    main()
