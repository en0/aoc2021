from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution


class SolutionTest(TestCase, TestCaseMixin):

    solution = Solution
    source = "sample.txt"
    given = 7


if __name__ == "__main__":
    main()
