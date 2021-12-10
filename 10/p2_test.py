from unittest import TestCase, main
from aocfw import TestCaseMixin
from p2 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 288957

    def test_completion(self):
        sol = Solution()
        self.assertEqual(sol.find_closing_string("[({(<(())[]>[[{[]{<()<>>"), "}}]])})]")
        self.assertEqual(sol.find_closing_string("[(()[<>])]({[<{<<[]>>("), ")}>]})")
        self.assertEqual(sol.find_closing_string("(((({<>}<{<{<>}{[]{[]{}"), "}}>}>))))")
        self.assertEqual(sol.find_closing_string("{<[[]]>}<{[{[{[]{()[[[]"), "]]}}]}]}>")
        self.assertEqual(sol.find_closing_string("<{([{{}}[<[[[<>{}]]]>[]]"), "])}>")

    def test_score(self):
        sol = Solution()
        self.assertEqual(sol.get_score("}}]])})]"), 288957)
        self.assertEqual(sol.get_score(")}>]})"), 5566)
        self.assertEqual(sol.get_score("}}>}>))))"), 1480781)
        self.assertEqual(sol.get_score("]]}}]}]}>"), 995444)
        self.assertEqual(sol.get_score("])}>"), 294)


if __name__ == '__main__':
    main()
