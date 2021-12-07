from unittest import TestCase, main
from aocfw import TestCaseMixin
from p2 import Solution


class SolutionTest(TestCase, TestCaseMixin):

    solution = Solution
    source = "sample.txt"
    given = 5

    def test_windowed(self):
        data = self.get_parsed_data()
        r = Solution().windowed(data)
        self.assertEqual(next(r), 607)
        self.assertEqual(next(r), 618)


if __name__ == "__main__":
    main()
