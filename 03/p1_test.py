from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = "sample.txt"
    given = 198

    def test_compute_gama_epsilon(self):
        data = self.get_parsed_data()
        gama, epsilon = Solution().compute_gama_epsilon(data)
        self.assertEqual(gama, '10110')
        self.assertEqual(epsilon, '01001')


if __name__ == "__main__":
    main()
