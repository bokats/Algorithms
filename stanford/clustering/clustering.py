from union_find import Vertex, Edge, UnionFind

class ClusteringMST(object):
    def __init__(self):
        self.edges = []
        self.union_find = UnionFind()

    def read_file(self, filename):
        file = open(filename, 'r')
        for line in file:
            line = line.split(" ")
            if len(line) > 1:
                v1 = Vertex(int(line[0]))
                v2 = Vertex(int(line[1]))
                self.edges.append(Edge(v1, v2, int(line[2])))
                self.union_find.add_vertex(v1)
                self.union_find.add_vertex(v2)

    def find_max_clustering_distance(self, k):
        self.edges = sorted(self.edges, key=lambda edge: edge.cost)
        idx = 0
        while len(self.union_find.leaders) > k:
            edge = self.edges[idx]
            v1_leader = self.union_find.find(edge.vertex_one.key)
            v2_leader = self.union_find.find(edge.vertex_two.key)
            if v1_leader != v2_leader:
                self.union_find.union(v1_leader.key, v2_leader.key)
            idx += 1

        return len(self.union_find.leaders)
c = ClusteringMST()
c.read_file('clustering.txt')
print(c.find_max_clustering_distance(4))
