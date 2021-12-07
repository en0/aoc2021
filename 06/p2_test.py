from unittest import TestCase, main
from aocfw import TestCaseMixin
from p2 import Solution


class SolutionTests(TestCase, TestCaseMixin):
    solution = Solution
    source = "sample.txt"
    given = 26984457539

    def test_get_counts(self):
        data = self.get_parsed_data()
        sol = Solution()
        sol.load_catalog(data)
        self.assertDictEqual(sol.fish, {0: 0, 1: 1, 2: 1, 3: 2, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0})

    def test_1_cycle(self):
        data = self.get_parsed_data()
        sol = Solution()
        sol.load_catalog(data)
        sol.cycle()
        self.assertDictEqual(sol.fish, {0: 1, 1: 1, 2: 2, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0})

if __name__ == "__main__":
    main()
