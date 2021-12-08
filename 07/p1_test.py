from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = "sample.txt"
    given = 37

    def test_find_target(self):
        data = self.get_parsed_data()
        self.assertEqual(Solution().get_target(data), 2)

    def test_get_fuel_cost_2(self):
        data = self.get_parsed_data()
        ans = Solution().get_fuel_cost(data, 2)
        self.assertEqual(ans, 37)

    def test_get_fuel_cost_1(self):
        data = self.get_parsed_data()
        ans = Solution().get_fuel_cost(data, 1)
        self.assertEqual(ans, 41)

    def test_get_fuel_cost_3(self):
        data = self.get_parsed_data()
        ans = Solution().get_fuel_cost(data, 3)
        self.assertEqual(ans, 39)

    def test_get_fuel_cost_10(self):
        data = self.get_parsed_data()
        ans = Solution().get_fuel_cost(data, 10)
        self.assertEqual(ans, 71)


if __name__ == "__main__":
    main()
