
class Node:
    def __init__(self, data):
        self.rank = 0
        self.data = data
        self.parent = None


class Kruskal:

    def findset(self, visited, node):
        start = node

        if node not in visited:
            return None

        # simple implementation, the recursive break with lot of level
        while visited[node].parent is not None:
            node = visited[node].parent.data

        # path compression
        if visited[start].parent is not None and visited[start].parent.data != visited[node].data:
            visited[start].parent = visited[node]

        return visited[node]

    def union(self, visited, src, dst):
        node_src = self.findset(visited, src)
        node_dst = self.findset(visited, dst)

        if node_src is None:
            node_src = Node(data=src)
            visited[src] = node_src

        if node_dst is None:
            node_dst = Node(data=dst)
            visited[dst] = node_dst

        if node_dst.rank > node_src.rank:
            node_src.parent = node_dst
            node_dst.rank += 1
        else:
            node_dst.parent = node_src
            node_src.rank += 1

        return visited

    def isCycle(self, visited, src, dst):
        node_src = self.findset(visited, src)
        node_dst = self.findset(visited, dst)

        return node_src is not None and node_dst is not None and \
               getattr(node_src, "data") and getattr(node_dst, "data") and node_src.data == node_dst.data

    def kruskal(self):
        # retrieves all edges of graph
        edges = self.edges()
        # dictionary that storage data linked to node / ex: "A": { rank: 0, data: "A", parent: "G" }
        visited = dict()
        # final list that storage the edges of minimal spanning tree
        mst = list()


        numOfNodes = self.number_of_nodes()

        # We sort the edges in order of weights
        edges.sort(key=lambda tup: tup[2])

        for edge in edges:
            if not self.isCycle(visited, edge[0], edge[1]):
                visited = self.union(visited, edge[0], edge[1])
                mst.append(edge)

                # whether all the nodes are processed, we get out
                if len(visited) == numOfNodes:
                    break

        return mst
