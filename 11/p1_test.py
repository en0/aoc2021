from unittest import TestCase, main, skip
from typing import List
from aocfw import TestCaseMixin
from io import StringIO
from p1 import Solution, Graph


class SolutionTests(TestCase, TestCaseMixin):
    solution = Solution
    source = 'sample.txt'
    given = 1656

    def test_graph_neighbors_00(self):
        graph = Graph()
        for y in range(5):
            for x in range(5):
                graph.add((x, y), (x * 10) + y)
        self.assertListEqual(graph.get_neighbors((0, 0)), [
            (1, 0),
            (0, 1), (1, 1)
        ])

    def test_graph_neighbors_11(self):
        graph = Graph()
        for y in range(5):
            for x in range(5):
                graph.add((x, y), (x * 10) + y)
        self.assertListEqual(graph.get_neighbors((1, 1)), [
            (0, 0), (1, 0), (2, 0),
            (0, 1), (2, 1),
            (0, 2), (1, 2), (2, 2)
        ])

    def test_graph_neighbors_44(self):
        graph = Graph()
        for y in range(5):
            for x in range(5):
                graph.add((x, y), (x * 10) + y)
        self.assertListEqual(graph.get_neighbors((4, 4)), [
            (3, 3), (4, 3),
            (3, 4),
        ])

    def test_parser(self):
        graph = next(self.get_parsed_data())
        self.assertListEqual(graph.get_neighbors((3, 3)), [
            (2, 2), (3, 2), (4, 2),
            (2, 3), (4, 3),
            (2, 4), (3, 4), (4, 4)
        ])

    def using_sample(self, sample: List[str]):
        self.source = None
        self.sample = StringIO("\n".join(sample))

    def test_cycle_1(self):
        self.using_sample([
            "11111",
            "19991",
            "19191",
            "19991",
            "11111",
        ])
        graph = next(self.get_parsed_data())
        Solution().cycle(graph)
        self.assertGraphEqual(graph, [
            [3, 4, 5, 4, 3],
            [4, 0, 0, 0, 4],
            [5, 0, 0, 0, 5],
            [4, 0, 0, 0, 4],
            [3, 4, 5, 4, 3],
        ])

    def test_cycle_2(self):
        self.using_sample([
            "11111",
            "19991",
            "19191",
            "19991",
            "11111",
        ])
        graph = next(self.get_parsed_data())
        sol = Solution()
        sol.cycle(graph)
        sol.cycle(graph)
        self.assertGraphEqual(graph, [
            [4, 5, 6, 5, 4],
            [5, 1, 1, 1, 5],
            [6, 1, 1, 1, 6],
            [5, 1, 1, 1, 5],
            [4, 5, 6, 5, 4],
        ])

    def test_cycle_with_sample_100(self):
        graph = next(self.get_parsed_data())
        sol = Solution()
        for _ in range(100):
            sol.cycle(graph)
        self.assertGraphEqual(graph, [
            [0, 3, 9, 7, 6, 6, 6, 8, 6, 6],
            [0, 7, 4, 9, 7, 6, 6, 9, 1, 8],
            [0, 0, 5, 3, 9, 7, 6, 9, 3, 3],
            [0, 0, 0, 4, 2, 9, 7, 8, 2, 2],
            [0, 0, 0, 4, 2, 2, 9, 8, 9, 2],
            [0, 0, 5, 3, 2, 2, 2, 8, 7, 7],
            [0, 5, 3, 2, 2, 2, 2, 9, 6, 6],
            [9, 3, 2, 2, 2, 2, 8, 9, 6, 6],
            [7, 9, 2, 2, 2, 8, 6, 8, 6, 6],
            [6, 7, 8, 9, 9, 9, 8, 7, 6, 6],
        ])

    def assertGraphEqual(self, graph: Graph, matrix: List[List[int]]):
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                self.assertEqual(graph.get_value((x, y)), val)


if __name__ == '__main__':
    main()
