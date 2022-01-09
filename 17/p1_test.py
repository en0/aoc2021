from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = None

    def test_loads(self):
        sol = self.solution.new()
        sol.load(self.get_parsed_data())
        self.assertTupleEqual(sol.boundary.x, (20, 30))
        self.assertTupleEqual(sol.boundary.y, (-10, -5))

    def test_contains(self):
        sol = self.solution.new()
        sol.load(self.get_parsed_data())
        self.assertEqual(sol.boundary.check_point((23, -8)), 0)
        self.assertEqual(sol.boundary.check_point((23, 0)), -1)
        self.assertEqual(sol.boundary.check_point((3, 0)), -1)
        self.assertEqual(sol.boundary.check_point((3, -8)), -1)
        self.assertEqual(sol.boundary.check_point((31, -8)), 1)
        self.assertEqual(sol.boundary.check_point((23, -15)), 1)
        self.assertEqual(sol.boundary.check_point((31, -15)), 1)

    def test_check_point(self):
        sol = self.solution.new()
        sol.load(self.get_parsed_data())
        self.assertIsNotNone(sol.shoot_prob((7,2)))
        self.assertIsNotNone(sol.shoot_prob((6,3)))
        self.assertIsNotNone(sol.shoot_prob((9,0)))
        self.assertIsNone(sol.shoot_prob((17,-4)))
        self.assertEqual(sol.shoot_prob((6,9)), 45)


if __name__ == '__main__':
    main()
