from unittest import TestCase, main
from aocfw import TestCaseMixin
from p2 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 2188189693529

    def test_compute_score(self):
        sol = self.solution.new()
        ans = sol.compute_score({
            "a": 100,
            "b": 99,
            "c": 50
        })
        self.assertEqual(ans, 50)

    def test_merge_dicts(self):
        sol = self.solution.new()
        ans = sol.merge_dict_counts(
            {"a": 10, "b": 5, "z": 1},
            {"a":1, "b": 6, "c": 1}
        )
        self.assertDictEqual(ans, {
            "a": 11,
            "b": 11,
            "c": 1,
            "z": 1
        })

    def test_count_chars(self):
        sol = self.solution.new()
        sol.load(self.get_parsed_data())
        ans = sol.count_chars("NN", 4)
        self.assertDictEqual(ans, {
            "B": 6,
            "C": 5,
            "N": 5,
        })

if __name__ == '__main__':
    main()
