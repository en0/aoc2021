from unittest import TestCase, main
from aocfw import TestCaseMixin
from p2 import Solution


class SolutionTest(TestCase, TestCaseMixin):

    solution = Solution
    source = "sample.txt"
    given = 1924


if __name__ == "__main__":
    main()
