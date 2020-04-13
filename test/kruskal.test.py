import random
import string
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from source.graph import Graph


class TestKruskal(unittest.TestCase):

    def test_with_initialization_list(self):
        data_graph = [
            ("A", "B", 7), ("A", "D", 5),
            ("B", "A", 7), ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
            ("C", "B", 8), ("C", "E", 5),
            ("D", "A", 5), ("D", "B", 9), ("D", "E", 15), ("D", "F", 6),
            ("E", "B", 7), ("E", "C", 5), ("E", "D", 15), ("E", "F", 8), ("E", "G", 9),
            ("F", "D", 6), ("F", "E", 8), ("F", "G", 11),
            ("G", "E", 9), ("G", "F", 11),
        ]

        # initialization graph
        graph = Graph(data_graph)

        # execution kruskal method
        edges = graph.kruskal()

        # checks tree returned by kruskal method
        self.assertEqual(len(edges), 6)
        self.assertEqual(edges, [
            ("A", "D", 5), ("C", "E", 5), ("D", "F", 6), ("A", "B", 7), ("B", "E", 7), ("E", "G", 9)])

    def test_with_initialization_dict(self):
        # with different weight for bi-directional / ex: "A" -[3]-> "B"
                                                       # "A" <-[8]- "B"
        data_graph = {
            "ABC":  {"2": 6, "&^%": 3, "grh": 4, "5748": 3},
            "2":    {"ABC": 1, "&^%": 4, "grh": 3, "5748": 4},
            "&^%":  {"ABC": 2, "2": 6, "grh": 3, "5748": 4},
            "grh":  {"ABC": 1, "2": 5, "&^%": 2, "5748": 2},
            "5748": {"ABC": 3, "2": 5, "&^%": 7, "grh": 4},
        }

        # initialization graph
        graph = Graph(data_graph)

        # execution kruskal method
        edges = graph.kruskal()

        # checks tree returned by kruskal method
        self.assertEqual(len(edges), 4)
        self.assertEqual(edges, [
            ("2", "ABC", 1), ("grh", "ABC", 1), ("&^%", "ABC", 2), ("grh", "5748", 2)])

    def test_load_with_1000000_edegs_1000_nodes(self):
        # defines random function
        def randomStringDigits(stringLength=6):
            lettersAndDigits = string.ascii_letters + string.digits
            return "".join(random.choice(lettersAndDigits) for i in range(stringLength))

        data_graph = dict()

        # graph creation with nodes
        for string_len in range(5, 11):
            for variant in range(1, 200):
                data_graph[randomStringDigits(string_len)] = dict()

        # for each node, we add all the other nodes as edges
        for node in data_graph:
            for node2 in data_graph:
                data_graph[node][node2] = random.randint(1, 99999)


        # initialization graph
        graph = Graph(data_graph)

        # execution kruskal method
        edges = graph.kruskal()

        self.assertEqual(len(edges), graph.number_of_nodes() - 1)


if __name__ == "__main__":
    unittest.main()
