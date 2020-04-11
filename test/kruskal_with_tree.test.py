import random
import string
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from source.graph import Graph

def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


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

        edges = graph.kruskalTree()

        print(edges)
        result = 0
        for edge in edges:
            result += edge[2]

        self.assertEqual(result, 39)

    def test_load(self):
        data_graph = dict()

        # creation des noeuds
        for string_len in range(5, 10):
            for variant in range(2, 1000):
                data_graph[randomStringDigits(string_len)] = dict()

        for node in data_graph:
            for node2 in data_graph:
                data_graph[node][node2] = random.randint(1, 99999)

        print(len(data_graph))

        # data_graph = [
        #     ("A", "D", 5), ("A", "B", 7),
        #     ("B", "A", 7), ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
        #     ("C", "B", 8), ("C", "E", 5),
        #     ("D", "A", 5), ("D", "B", 9), ("D", "E", 15), ("D", "F", 6),
        #     ("E", "B", 7), ("E", "C", 5), ("E", "D", 15), ("E", "F", 8), ("E", "G", 9),
        #     ("F", "D", 6), ("F", "E", 8), ("F", "G", 11),
        #     ("G", "F", 11), ("G", "E", 9),
        # ]
        #
        # graph = Graph(data_graph)
        #
        # edges = graph.kruskalTree()
        #
        # print(edges)
        # result = 0
        # for edge in edges:
        #     result += edge[2]
        #
        # self.assertEqual(result, 39)


if __name__ == '__main__':
    unittest.main()
