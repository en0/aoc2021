import unittest
from p1 import Solution
from parser import SubmarineInstructionParser


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.data = iter([
            ("forward", 5),
            ("down", 5),
            ("forward", 8),
            ("up", 3),
            ("down", 8),
            ("forward", 2),
        ])

    def test_parser(self):
        parser = SubmarineInstructionParser()
        gen = parser.parse(iter(["forward 5"]))

        inst, val = next(gen)
        self.assertEqual(inst, "forward")
        self.assertEqual(val, 5)


    def test_given(self):
        self.assertEqual(Solution().solve(self.data), 150)


if __name__ == "__main__":
    unittest.main()
