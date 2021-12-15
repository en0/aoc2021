from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 1588

    def test_step(self):
        data = self.get_parsed_data()
        sol = self.solution.new()
        sol.load(data)
        self.assertEqual(sol.poly, "NNCB")
        sol.do_insert_step()
        self.assertEqual(sol.poly, "NCNBCHB")
        sol.do_insert_step()
        self.assertEqual(sol.poly, "NBCCNBBBCBHCB")
        sol.do_insert_step()
        self.assertEqual(sol.poly, "NBBBCNCCNBBNBNBBCHBHHBCHB")
        ...


if __name__ == '__main__':
    main()
