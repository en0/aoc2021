from unittest import TestCase, main
from io import StringIO
from aocfw import TestCaseMixin
from p1 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 26

    def test_parser_simple(self):
        self.source = None
        self.sample = StringIO(
            "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
            " | cdfeb fcadb cdfeb cdbaf"
        )
        gen = self.get_parsed_data()
        self.assertEqual(("cdfeb", "fcadb", "cdfeb", "cdbaf"), next(gen))

    def test_parser_multi(self):
        actual = list(self.get_parsed_data())
        expected = [
            ("fdgacbe", "cefdb", "cefbgd", "gcbe"),
            ("fcgedb", "cgb", "dgebacf", "gc"),
            ("cg", "cg", "fdcagb", "cbg"),
            ("efabcd", "cedba", "gadfec", "cb"),
            ("gecf", "egdcabf", "bgf", "bfgea"),
            ("gebdcfa", "ecba", "ca", "fadegcb"),
            ("cefg", "dcbef", "fcge", "gbcadfe"),
            ("ed", "bcgafe", "cdgba", "cbgef"),
            ("gbdfcae", "bgc", "cg", "cgb"),
            ("fgae", "cfgab", "fg", "bagce"),
        ]
        self.assertListEqual(expected, actual)

    def test_count_easy_ones(self):
        self.assertEqual(Solution().count_easy_ones(("cg", "cg", "fdcagb", "cbg")), 3)
        self.assertEqual(Solution().count_easy_ones(("ed", "bcgafe", "cdgba", "cbgef")), 1)


if __name__ == '__main__':
    main()

