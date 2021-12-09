from unittest import TestCase, main, skip
from io import StringIO
from aocfw import TestCaseMixin
from p1 import Solution, Graph


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 15

    def test_graph(self):
        g = Graph()
        g.add_vertex((1, 1), 1)
        g.add_vertex((4, 4,), 4)
        g.add_vertex((5, 5), 5)
        g.add_vertex((6, 6), 6)
        g.add_edge((1, 1), (5, 5))
        g.add_edge((5, 5), (6, 6))
        self.assertSetEqual(g.get_neighbors((1, 1)), set([(5, 5)]))
        self.assertSetEqual(g.get_neighbors((5, 5)), set([(1, 1), (6, 6)]))
        self.assertSetEqual(g.get_neighbors((4, 4)), set())
        self.assertEqual(g.get_value((1, 1)), 1)
        self.assertEqual(g.get_value((4, 4)), 4)
        self.assertEqual(g.get_value((5, 5)), 5)

    def test_parser(self):
        data = self.get_parsed_data()
        graph: Graph = next(data)
        self.assertEqual(graph.get_value((0, 0)), 2)
        self.assertEqual(graph.get_value((0, 4)), 9)
        self.assertEqual(graph.get_value((9, 0)), 0)
        self.assertEqual(graph.get_value((9, 4)), 8)
        self.assertSetEqual(graph.get_neighbors((0, 0)), set([(0, 1), (1, 0)]))
        self.assertSetEqual(graph.get_neighbors((1, 1)), set([(0, 1), (1, 0), (1, 2), (2, 1)]))
        self.assertSetEqual(graph.get_neighbors((9, 4)), set([(8, 4), (9, 3)]))

    def test_edgecase1(self):
        self.source = None
        self.given = 1
        self.sample = StringIO("\n".join([
            "9999999999",
            "9999999999",
            "9999909999",
            "9999999999",
            "9999999999",
        ]))
        self.test_given()


if __name__ == '__main__':
    main()
