import unittest
from p2 import Solution

from bingo import BingoBoard


class SolutionTest(unittest.TestCase):
    def setUp(self):

        board1 = BingoBoard()
        board1.append([22, 13, 17, 11, 0])
        board1.append([8, 2, 23, 4, 24])
        board1.append([21, 9, 14, 16, 7])
        board1.append([6, 10, 3, 18, 5])
        board1.append([1, 12, 20, 15, 19])

        board2 = BingoBoard()
        board2.append([3, 15, 0, 2, 22])
        board2.append([9, 18, 13, 17, 5])
        board2.append([19,  8, 7, 25, 23])
        board2.append([20, 11, 10, 24, 4])
        board2.append([14, 21, 16, 12, 6])

        board3 = BingoBoard()
        board3.append([14, 21, 17, 24, 4])
        board3.append([10, 16, 15, 9, 19])
        board3.append([18, 8, 23, 26, 20])
        board3.append([22, 11, 13, 6, 5])
        board3.append([2, 0, 12, 3, 7])

        self.data = iter([
            [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1],
            [board1, board2, board3]
        ])

    def test_given(self):
        self.assertEqual(Solution().solve(self.data), 1924)


if __name__ == "__main__":
    unittest.main()
