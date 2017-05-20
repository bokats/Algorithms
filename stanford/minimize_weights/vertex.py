class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.out_edges = []

    def add_out_edge(self, edge):
        self.out_edges.append(edge)

class Edge(object):
    def __init__(self, start_vertex, end_vertex, cost):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.cost = cost


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
