from unittest import TestCase, main
from bingo import BingoBoard


class SolutionTest(TestCase):

    def setUp(self):
        board = BingoBoard()
        board.append([14, 21, 17, 24, 4])
        board.append([10, 16, 15, 9, 19])
        board.append([18, 8, 23, 26, 20])
        board.append([22, 11, 13, 6, 5])
        board.append([2, 0, 12, 3, 7])
        self.board = board

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
    main()
