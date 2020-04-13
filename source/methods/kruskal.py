
class Kruskal:

    def findset(self, relation, graph, node):
        if node not in relation:
            return None

        # keeps the first node
        start = relation[node]
        # values that represent the parent / ex: 4 so parent 4 index or -3 so no parent
        parent = graph[start]
        # keeps the index / ex: 1 => 5 => -4 , index 5
        index = start

        # simple implementation, the recursive break with lot of level
        while parent >= 0:
            index = parent
            parent = graph[parent]

        # path compression
        if graph[start] != graph[index]:
            graph[start] = index

        return index

    def union(self, relation, graph, src, dst):
        node_src = self.findset(relation, graph, src)
        node_dst = self.findset(relation, graph, dst)

        if node_src is None:
            node_src = len(relation)
            relation[src] = node_src

        if node_dst is None:
            node_dst = len(relation)
            relation[dst] = node_dst

        # whether the rank of "dst" is at most that "src" / ex: -6 > -4
        if graph[node_dst] < graph[node_src]:
            graph[node_dst] += graph[node_src]
            graph[node_src] = node_dst
        else:
            graph[node_src] += graph[node_dst]
            graph[node_dst] = node_src

    def isCycle(self, relation, graph, src, dst):
        node_src = self.findset(relation, graph, src)
        node_dst = self.findset(relation, graph, dst)

        return node_src is not None and node_dst is not None and node_src == node_dst

    def kruskal(self):
        # retrieves all edges of graph
        edges = self.edges()
        # retrieves the numbers of nodes
        numOfNodes = self.number_of_nodes()
        # dictionary that storage data linked to node / ex: "A": { rank: 0, data: "A", parent: "G" }
        relation = dict()
        # final list that storage the edges of minimal spanning tree
        mst = list()

        # graph initialization
        graph = [-1 for i in range(numOfNodes + 1)]

        # We sort the edges in order of weights
        edges.sort(key=lambda tup: tup[2])

        for edge in edges:
            if not self.isCycle(relation, graph, edge[0], edge[1]):
                self.union(relation, graph, edge[0], edge[1])
                mst.append(edge)

                # whether all the nodes are processed, we get out
                if len(mst) == (numOfNodes - 1):
                    break

        return mst
