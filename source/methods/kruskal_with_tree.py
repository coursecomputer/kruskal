
class Node:
    def __init__(self, data):
        self.rank: int = 0
        self.data: str = data
        self.parent: Node = None


class KruskalTree:

    def findTree(self, visited, vertice):
        if vertice not in visited:
            return None

        if visited[vertice].parent is None:
            return visited[vertice]

        return self.findTree(visited, visited[vertice].parent.data)

    def unionTree(self, visited, v1, v2):
        nodeV1 = self.findTree(visited, v1)
        nodeV2 = self.findTree(visited, v2)

        if nodeV1 is None:
            nodeV1 = Node(data=v1)
            visited[v1] = nodeV1

        if nodeV2 is None:
            nodeV2 = Node(data=v2)
            visited[v2] = nodeV2

        if nodeV2.rank > nodeV1.rank:
            nodeV1.parent = nodeV2
        else:
            nodeV2.parent = nodeV1

        return visited

    def isCycleTree(self, visited, v1, v2):
        nodeV1 = self.findTree(visited, v1)
        nodeV2 = self.findTree(visited, v2)

        return nodeV1 is not None and nodeV2 is not None and \
               getattr(nodeV1, "data") and getattr(nodeV2, "data") and nodeV1.data == nodeV2.data

    def kruskalTree(self):
        edges = self.edges()
        visited = dict()
        mst = list()

        # We sort the edges in order of weights
        edges.sort(key=lambda tup: tup[2])

        for edge in edges:
            if not self.isCycleTree(visited, edge[0], edge[1]):
                visited = self.unionTree(visited, edge[0], edge[1])
                mst.append(edge)

        for key in visited:
            print(key , ' => ', visited[key].parent.data if visited[key].parent is not None else None)
        return mst
