from unittest import TestCase, main, skip
from io import StringIO
from aocfw import TestCaseMixin
from p2 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 61229

    def get_one_sample(self):
        self.source = None
        self.sample = StringIO(
            "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
            " | cdfeb fcadb cdfeb cdbaf"
        )
        return next(self.get_parsed_data())

    def test_parser_simple(self):
        _in, _out = self.get_one_sample()
        self.assertEqual((
            set("acedgfb"), set("cdfbe"), set("gcdfa"), set("fbcad"), set("dab"),
            set("cefabd"), set("cdfgeb"), set("eafb"), set("cagedb"), set("ab")), _in)
        self.assertEqual((set("cdfeb"), set("fcadb"), set("cdfeb"), set("cdbaf")), _out)

    def test_collect_by_count(self):
        sol = Solution()
        result = sol.collect_by_count((
            "acedgfb", "cdfbe", "gcdfa", "fbcad", "dab",
            "cefabd", "cdfgeb", "eafb", "cagedb", "ab"))
        self.assertDictEqual({
            2: sorted(result[2]),
            3: sorted(result[3]),
            4: sorted(result[4]),
            5: sorted(result[5]),
            6: sorted(result[6]),
            7: sorted(result[7]),
        }, {
            2: ["ab"],
            3: ["dab"],
            4: ["eafb"],
            5: ["cdfbe", "fbcad", "gcdfa"],
            6: ["cagedb", "cdfgeb", "cefabd"],
            7: ["acedgfb"]})

    def test_map_values_1(self):
        data, _ = self.get_one_sample()
        sol = Solution()
        result = sol.map_values(data)
        self.assertEqual(result["ab"], "1")

    def test_map_values_4(self):
        data, _ = self.get_one_sample()
        sol = Solution()
        result = sol.map_values(data)
        self.assertEqual(result["abef"], "4")

    def test_map_values_7(self):
        data, _ = self.get_one_sample()
        sol = Solution()
        result = sol.map_values(data)
        self.assertEqual(result["abd"], "7")

    def test_map_values_8(self):
        data, _ = self.get_one_sample()
        sol = Solution()
        result = sol.map_values(data)
        self.assertEqual(result["abcdefg"], "8")

    def test_map_values_9(self):
        data, _ = self.get_one_sample()
        sol = Solution()
        result = sol.map_values(data)
        self.assertEqual(result["abcdef"], "9")

    def test_map_values_3(self):
        data, _ = self.get_one_sample()
        sol = Solution()
        result = sol.map_values(data)
        self.assertEqual(result["abcdf"], "3")

    def test_map_values_6(self):
        data, _ = self.get_one_sample()
        sol = Solution()
        result = sol.map_values(data)
        self.assertEqual(result["bcdefg"], "6")

    def test_map_values_0(self):
        data, _ = self.get_one_sample()
        sol = Solution()
        result = sol.map_values(data)
        self.assertEqual(result["abcdeg"], "0")

    def test_map_values_5(self):
        data, _ = self.get_one_sample()
        sol = Solution()
        result = sol.map_values(data)
        self.assertEqual(result["bcdef"], "5")

    def test_map_values_2(self):
        data, _ = self.get_one_sample()
        sol = Solution()
        result = sol.map_values(data)
        self.assertEqual(result["acdfg"], "2")

    def test_decode_value(self):
        data, val = self.get_one_sample()
        sol = Solution()
        mapping = sol.map_values(data)
        val = sol.decode_value(mapping, val)
        self.assertEqual(val, 5353)


if __name__ == '__main__':
    main()

