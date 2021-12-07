from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution
from parser import SubmarineInstructionParser


class SolutionTest(TestCase, TestCaseMixin):

    solution = Solution
    source = "sample.txt"
    given = 150

    def test_parser(self):
        data = self.get_parsed_data()
        inst, val = next(data)
        self.assertEqual(inst, "forward")
        self.assertEqual(val, 5)


if __name__ == "__main__":
    main()
