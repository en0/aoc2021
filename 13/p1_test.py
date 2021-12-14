from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 17

    def test_x_fold(self):
        data = self.get_parsed_data()
        sol = Solution()
        sol.load_matrix(data)
        sol.fold_y(7)
        self.assertMatrixEqual(sol.matrix, [
            [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 1, 0, 2, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])

    def assertMatrixEqual(self, a, b):
        for a_row, b_row in zip(a, b):
            for a_cell, b_cell in zip(a_row, b_row):
                self.assertEqual(a_cell, b_cell, f"Looks like this:\n{a}")

if __name__ == '__main__':
    main()
