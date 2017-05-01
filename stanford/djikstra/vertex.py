class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.shortest_distance = 0
        self.shortest_path = []
        self.out_edges = []

    def get_key(self):
        return self.key

    def get_shortest_distance(self):
        return self.shortest_distance

    def get_path(self):
        return self.shortest_path

    def get_out_edges(self):
        return self.out_edges

    def set_shortest_distance(self, new_distance):
        self.shortest_distance = new_distance
        return self.shortest_distance

    def set_path(self, new_path):
        self.shortest_path = new_path
        return self.shortest_path

    def add_out_edge(self, edge):
        self.out_edges.append(edge)

class Edge(object):
    def __init__(self, start_vertex, end_vertex, distance):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.distance = distance

    def get_start_vertex(self):
        return self.start_vertex

    def get_end_vertex(self):
        return self.end_vertex

    def get_distance(self):
        return self.distance

# Tests

# n = Vertex()
# assert n.get_shortest_distance() == 0
# assert n.get_path() == []
# assert n.get_out_edges() == []
#
# n.set_shortest_distance(3)
# assert n.get_shortest_distance() == 3
# n2 = Vertex()
# n3 = Vertex()
# n.set_path([n2, n3])
# assert n.get_path() == [n2,n3]
#
# e = Edge(n, n2, 5)
#
# n.add_out_edge(e)
# assert n.get_out_edges() == [e]
#
# assert e.get_start_vertex() == n
# assert e.get_end_vertex() == n2
# assert e.get_distance() == 5
