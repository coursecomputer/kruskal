
class Kruskal:

    def find(self, relation, graph, node):
        """Find the parent of node passed in parameter

        Parameters
        ----------
        relation : dict
            Represents the link between the node name and the cycle graph index
        graph : list
            Represents the cycle graph
        node : str
            Name of node

        Returns
        -------
        int
            The index of parent
        None
            Whether the node isn't in the dictionary
        """

        if node not in relation:
            return None

        # keeps the first node for the path compression
        start = relation[node]
        # keeps the index for return it
        index = start
        # value which represents either the next index then it will be stored in the variable "index"
        # or a negative number which means that it has no parent
        parent = graph[start]

        # continue until "parent" variable whether negative
        while parent >= 0:
            index = parent
            parent = graph[parent]

        # path compression
        # if the index of the start node is different from the parent node to avoid overwriting the rank then we set it
        if start != index:
            graph[start] = index

        return index

    def union(self, relation, graph, src, dst):
        node_src = self.find(relation, graph, src)
        node_dst = self.find(relation, graph, dst)

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
        node_src = self.find(relation, graph, src)
        node_dst = self.find(relation, graph, dst)

        return node_src is not None and node_dst is not None and node_src == node_dst

    def kruskal(self):
        # retrieves all edges of graph
        edges = self.edges()
        # retrieves the numbers of nodes
        numOfNodes = self.number_of_nodes()
        # dictionary that storage data node to index graph / ex: { "A": 0, "B": 1 }
        relation = dict()
        # final list that storage the edges of minimal spanning tree
        mst = list()

        # graph initialization
        graph = [-1 for i in range(numOfNodes + 1)]

        # sort the edges in order of weights
        edges.sort(key=lambda tup: tup[2])

        for edge in edges:
            if not self.isCycle(relation, graph, edge[0], edge[1]):
                self.union(relation, graph, edge[0], edge[1])
                mst.append(edge)

                # whether all the nodes are processed, we get out
                if len(mst) == (numOfNodes - 1):
                    break

        return mst
