from unittest import TestCase, main, skip
from aocfw import TestCaseMixin
from p2 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = "sample.txt"
    given = 168

    def test_triangular_numbers(self):
        self.assertEqual(Solution().get_triangular_number(3), 6)
        self.assertEqual(Solution().get_triangular_number(10), 55)
        self.assertEqual(Solution().get_triangular_number(1), 1)
        self.assertEqual(Solution().get_triangular_number(0), 0)

    def test_get_target(self):
        data = self.get_parsed_data()
        self.assertEqual(Solution().get_target(data), (4, 5))

    def test_get_fuel_cost_2(self):
        data = self.get_parsed_data()
        ans = Solution().get_fuel_cost(data, 2)
        self.assertEqual(ans, 206)

    def test_get_fuel_cost_5(self):
        data = self.get_parsed_data()
        ans = Solution().get_fuel_cost(data, 5)
        self.assertEqual(ans, 168)


if __name__ == "__main__":
    main()
