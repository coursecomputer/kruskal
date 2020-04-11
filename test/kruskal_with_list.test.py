import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from source.graph import Graph


class TestSum(unittest.TestCase):

    def test_sum(self):
        data_graph = [
            ("A", "D", 5), ("A", "B", 7),
            ("B", "A", 7), ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
            ("C", "B", 8), ("C", "E", 5),
            ("D", "A", 5), ("D", "B", 9), ("D", "E", 15), ("D", "F", 6),
            ("E", "B", 7), ("E", "C", 5), ("E", "D", 15), ("E", "F", 8), ("E", "G", 9),
            ("F", "D", 6), ("F", "E", 8), ("F", "G", 11),
            ("G", "F", 11), ("G", "E", 9),
        ]

        graph = Graph(data_graph)

        edges = graph.kruskalList()

        print(edges)
        result = 0
        for edge in edges:
            result += edge[2]

        self.assertEqual(result, 39)


if __name__ == '__main__':
    unittest.main()
