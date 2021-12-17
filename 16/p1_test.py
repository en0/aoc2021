from unittest import TestCase, main
from typing import List
from io import StringIO
from aocfw import TestCaseMixin
from p1 import Solution, Operation
from contextlib import contextmanager


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 6

    def test_parser(self):
        data = self.get_parsed_data()
        self.assertEqual(next(data), "110100101111111000101000")
        with self.context_sample(["38006F45291200"]) as data:
            self.assertEqual(
                next(data),
                "00111000000000000110111101000101001010010001001000000000"
            )

    def test_litteral(self):
        data = self.get_parsed_data()
        sol = self.solution.new()
        sol.load(data)
        op = sol.read_packet()
        self.assertEqual(op.get_value(), 2021)

    def test_operator(self):
        sol = self.solution.new()
        with self.context_sample(["38006F45291200"]) as data:
            sol.load(data)
            op = sol.read_packet()
            self.assertEqual(str(op), "O[L10,L20]")

    def test_case_1(self):
        self.assertVersionSum("8A004A801A8002F478", 16)

    def test_case_2(self):
        self.assertVersionSum("620080001611562C8802118E34", 12)

    def test_case_3(self):
        self.assertVersionSum("C0015000016115A2E0802F182340", 23)

    def test_case_4(self):
        self.assertVersionSum("A0016C880162017C3686B18A3D4780", 31)

    def assertVersionSum(self, data, value):
        sol = self.solution.new()
        with self.context_sample([data]) as data:
            sol.load(data)
            op = sol.read_packet()
            self.assertEqual(op.sum_version(), value)


if __name__ == '__main__':
    main()
