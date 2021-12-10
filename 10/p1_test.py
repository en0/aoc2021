from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 26397

    def test_legal_lines(self):
        sol = Solution()
        self.assertEqual(sol.compute_line_score("()"), 0)
        self.assertEqual(sol.compute_line_score("[]"), 0)
        self.assertEqual(sol.compute_line_score("([])"), 0)
        self.assertEqual(sol.compute_line_score("{()()()}"), 0)
        self.assertEqual(sol.compute_line_score("<([{}])>"), 0)
        self.assertEqual(sol.compute_line_score("[<>({}){}[([])<>]]"), 0)
        self.assertEqual(sol.compute_line_score("(((((((((())))))))))"), 0)

    def test_illegal_lines(self):
        sol = Solution()
        self.assertGreater(sol.compute_line_score("(]"), 0)
        self.assertGreater(sol.compute_line_score("{()()()>"), 0)
        self.assertGreater(sol.compute_line_score("(((()))}"), 0)
        self.assertGreater(sol.compute_line_score("<([]){()}[{}])"), 0)

    def test_line_value(self):
        sol = Solution()
        self.assertEqual(sol.compute_line_score("{([(<{}[<>[]}>{[]{[(<()>"), 1197)



if __name__ == '__main__':
    main()
