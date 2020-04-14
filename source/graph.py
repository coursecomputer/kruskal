from .methods.kruskal import Kruskal


class Graph(Kruskal):

    def __init__(self, data=None):
        super().__init__()

        # Dictionary with node and edges
        if type(data) == dict:
            self.graph = data
        # List with edges only
        elif type(data) == list:
            self.graph = dict()

            for edge in data:
                if edge[0] in self.graph:
                    self.graph[edge[0]][edge[1]] = edge[2]
                else:
                    self.graph[edge[0]] = {
                        edge[1]: edge[2]
                    }
        # Default empty dictionary
        else:
            self.graph = dict()

    def edges(self):
        edges = list()

        for node in self.graph:
            for neighbourNode in self.graph[node]:
                edges.append(tuple([node, neighbourNode, self.graph[node][neighbourNode]]))

        return edges

    def number_of_nodes(self):
        return len(self.graph)
