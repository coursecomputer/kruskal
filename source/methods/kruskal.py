
class Kruskal:

    def find(self, relation, graph, node):
        """Find the parent of node passed in parameter

        Args:
            relation (dict): Links between the node name and the cycle graph index
            graph (list): The cycle graph
            node (str): Name of node

        Returns:
            int: The index of parent
        """

        # if the node does not exist in the "relationship" dictionary, we initialize it
        if node not in relation:
            # assign node relation with the size of dictionary because it's equal to "graph" index
            relation[node] = len(relation)
            return relation[node]

        # keeps the first node for the path compression
        start = relation[node]
        # keeps the index to return it
        index = start
        # value which represents either the next index then it will be stored in the variable "index"
        # or a negative number which means that it has no parent
        parent = graph[start]

        # continue until "parent" variable is negative
        while parent >= 0:
            index = parent
            parent = graph[parent]

        # path compression
        # if the starting node index is different from the parent node to avoid overwriting the rank then we set it
        if start != index:
            graph[start] = index

        return index

    def union(self, relation, graph, src, dst):
        """Find the parent of src and dst and merge them together

        Args:
            relation (dict): Links between the node name and the cycle graph index
            graph (list): The cycle graph
            src (str): Name of the starting node
            dst (str): Name of the ending node
        """

        node_src = self.find(relation, graph, src)
        node_dst = self.find(relation, graph, dst)

        # whether the rank of "dst" have higher negative rank than "src" / ex: -6 > -4
        if graph[node_dst] < graph[node_src]:
            graph[node_dst] += graph[node_src]
            graph[node_src] = node_dst
        else:
            graph[node_src] += graph[node_dst]
            graph[node_dst] = node_src

    def is_cycle(self, relation, graph, src, dst):
        """Checks if there's a cycle

        Args:
            relation (dict): Links between the node name and the cycle graph index
            graph (list): The cycle graph
            src (str): Name of the starting node
            dst (str): Name of the ending node

        Returns:
            bool: cycle True / no cycle False
        """

        node_src = self.find(relation, graph, src)
        node_dst = self.find(relation, graph, dst)

        return node_src == node_dst

    def kruskal(self):
        """Find and return the minimal spanning tree of a graph

        Returns:
            list: List of edges like [(A, B, 3), (A, C, 7)]
        """

        # retrieves all edges of graph
        edges = self.edges()
        # retrieves the numbers of nodes
        num_of_nodes = self.number_of_nodes()
        # dictionary that store data node to index graph / ex: { "A": 0, "B": 1 }
        relation = dict()
        # final list storing the edges of the minimal spanning tree
        mst = list()

        # graph initialization
        graph = [-1 for _ in range(num_of_nodes + 1)]

        # sort the edges by weights
        edges.sort(key=lambda tup: tup[2])

        for edge in edges:
            if not self.is_cycle(relation, graph, edge[0], edge[1]):
                self.union(relation, graph, edge[0], edge[1])
                mst.append(edge)

                # when all the nodes have been processed we get out
                if len(mst) == (num_of_nodes - 1):
                    break

        return mst
