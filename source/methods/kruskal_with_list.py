
class KruskalList:

    def find(self, visited, v1, v2):
        for union in visited:
            if v1 in union and v2 in union:
                return True
        return False

    def union(self, visited, v1, v2):
        s1 = -1
        s2 = -1

        for index in range(len(visited)):
            if v1 in visited[index]:
                s1 = index
            if v2 in visited[index]:
                s2 = index

        if s1 == -1 and s2 == -1:
            visited.append(list([v1, v2]))
        elif s1 == -1:
            visited[s2].append(v1)
        elif s2 == -1:
            visited[s1].append(v2)
        else:
            visited[s1] = list(set().union(visited[s1], visited[s2]))
            del visited[s2]

        return visited

    def isCycle(self, visited, v1, v2):
        return self.find(visited, v1, v2)

    def kruskalList(self):
        edges = self.edges()
        visited = list()
        mst = list()

        # We sort the edges in order of weights
        edges.sort(key=lambda tup: tup[2])

        for edge in edges:
            if not self.isCycle(visited, edge[0], edge[1]):
                visited = self.union(visited, edge[0], edge[1])
                mst.append(edge)

        return mst
