from unittest import TestCase, main
from io import StringIO
from aocfw import TestCaseMixin
from p2 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 315

    def use_sample(self, val):
        self.source = None
        self.sample = StringIO("\n".join(val))
        return self.get_parsed_data()

    def test_expand_map(self):
        data = self.use_sample(["8"])
        sol = self.solution.new()
        sol.load(data)
        sol.expand()
        # dealing with that Tile object
        ans = {(x, y): v.h_cost for (x, y), v in sol.matrix.items()}
        self.assertEqual(sol.end, (4, 4))
        self.assertDictEqual(ans, {
            (0, 0): 8, (1, 0): 9, (2, 0): 1, (3, 0): 2, (4, 0): 3,
            (0, 1): 9, (1, 1): 1, (2, 1): 2, (3, 1): 3, (4, 1): 4,
            (0, 2): 1, (1, 2): 2, (2, 2): 3, (3, 2): 4, (4, 2): 5,
            (0, 3): 2, (1, 3): 3, (2, 3): 4, (3, 3): 5, (4, 3): 6,
            (0, 4): 3, (1, 4): 4, (2, 4): 5, (3, 4): 6, (4, 4): 7,
        })


if __name__ == '__main__':
    main()
