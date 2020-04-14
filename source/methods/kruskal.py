
class Kruskal:

    def find(self, relation, graph, node):
        """Find the parent of node passed in parameter

        Args:
            relation (dict): Represents the link between the node name and the cycle graph index
            graph (list): Represents the cycle graph
            node (str): Name of node

        Returns:
            int: The index of parent
        """

        # if the node does not exist in the "relationship" dictionary, we initialize
        if node not in relation:
            # sets node with the size of dictionary because it's equal to "graph" index
            relation[node] = len(relation)
            return relation[node]

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
        """Finds the parent of src and dst to merge them together

        Args:
            relation (dict): Represents the link between the node name and the cycle graph index
            graph (list): Represents the cycle graph
            src (str): Name of the start node
            dst (str): Name of the end node
        """

        node_src = self.find(relation, graph, src)
        node_dst = self.find(relation, graph, dst)

        # whether the rank of "dst" is at most that "src" / ex: -6 > -4
        if graph[node_dst] < graph[node_src]:
            graph[node_dst] += graph[node_src]
            graph[node_src] = node_dst
        else:
            graph[node_src] += graph[node_dst]
            graph[node_dst] = node_src

    def isCycle(self, relation, graph, src, dst):
        """Checks if there's a cycle

        Args:
            relation (dict): Represents the link between the node name and the cycle graph index
            graph (list): Represents the cycle graph
            src (str): Name of the start node
            dst (str): Name of the end node

        Returns:
            bool: cycle True / no cycle False
        """

        node_src = self.find(relation, graph, src)
        node_dst = self.find(relation, graph, dst)

        return node_src == node_dst

    def kruskal(self):
        """Find and return the minimal tree of a graph

        Returns:
            list: List of edges like [(A, B, 3), (A, C, 7)]
        """

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
