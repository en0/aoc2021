import unittest
from io import StringIO
from bingo import BingoParser, BingoBoard


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.data = StringIO("\n".join([
            "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
            "",
            "22 13 17 11  0",
            "8  2 23  4 24",
            "21  9 14 16  7",
            "6 10  3 18  5",
            "1 12 20 15 19",
            "",
            "3 15  0  2 22",
            "9 18 13 17  5",
            "19  8  7 25 23",
            "20 11 10 24  4",
            "14 21 16 12  6",
            "",
            "14 21 17 24  4",
            "10 16 15  9 19",
            "18  8 23 26 20",
            "22 11 13  6  5",
            "2  0 12  3  7",
        ]))

        board = BingoBoard()
        board.append([14, 21, 17, 24, 4])
        board.append([10, 16, 15, 9, 19])
        board.append([18, 8, 23, 26, 20])
        board.append([22, 11, 13, 6, 5])
        board.append([2, 0, 12, 3, 7])
        self.board = board

    def test_called_numbers(self):
        gen = BingoParser().parse(self.data)
        self.assertListEqual(list(next(gen)), [
            7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21,
            24, 10, 16, 13, 6, 15, 25, 12, 22, 18,
            20, 8, 19, 3, 26, 1
        ])

    def test_boards_are_boards(self):
        gen = BingoParser().parse(self.data)
        next(gen)
        boards = list(next(gen))
        self.assertEqual(len(boards), 3)
        for board in boards:
            self.assertIsInstance(board, BingoBoard)

    def test_board_skip_mark(self):
        self.assertFalse(self.board.mark(-1))

    def test_board_horizontal_bingo(self):
        for v, s in zip([22, 11, 13, 6, 5], [False, False, False, False, True]):
            self.assertEqual(self.board.mark(v), s)

    def test_board_vertical_bingo(self):
        for v, s in zip([21, 16, 8, 11, 0], [False, False, False, False, True]):
            self.assertEqual(self.board.mark(v), s)

    def test_board_score(self):
        for v in [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]:
            self.board.mark(v)
        self.assertTrue(self.board.check_board())
        self.assertEqual(self.board.get_score(), 188)


if __name__ == "__main__":
    unittest.main()
