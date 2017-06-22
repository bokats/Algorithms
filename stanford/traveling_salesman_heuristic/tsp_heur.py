from math import inf
from heap import MinHeap, Node
import random

class Prims(object):
    def __init__(self):
        self.vertices = {}

    def read_file(self, filename):
        file = open(filename, 'r')
        for line in file:
            edge = line.split(" ")
            for i in range(len(edge)):
                edge[i] = int(edge[i])

            if len(edge) > 2:
                if edge[0] not in self.vertices.keys():
                    self.vertices[edge[0]] = Vertex(edge[0])
                if edge[1] not in self.vertices.keys():
                    self.vertices[edge[1]] = Vertex(edge[1])
                new_edge1 = Edge(self.vertices[edge[0]], self.vertices[edge[1]], edge[2])
                new_edge2 = Edge(self.vertices[edge[1]], self.vertices[edge[0]], edge[2])
                self.vertices[edge[0]].add_out_edge(new_edge1)
                self.vertices[edge[1]].add_out_edge(new_edge2)

    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex

    def find_min_spanning_tree(self):
        result = 0
        current_vertex = self.vertices[1]
        visited = set([current_vertex.key])
        heap = MinHeap()

        for edge in current_vertex.out_edges:
            heap.insert(Node(edge.cost, edge))

        while len(visited) != len(self.vertices):

            while True:
                min_node = heap.extract_min()
                min_edge = min_node.edge
                min_cost = min_node.value
                if min_edge.end_vertex.key not in visited:
                    break

            result += min_cost
            visited.add(min_edge.end_vertex.key)
            current_vertex = min_edge.end_vertex

            for edge in current_vertex.out_edges:
                if edge.end_vertex not in visited:
                    heap.insert(Node(edge.cost, edge))

        return result


# v1 = Vertex(1)
# v2 = Vertex(2)
# v3 = Vertex(3)
# v4 = Vertex(4)
# e1 = Edge(v1, v2, 1)
# e2 = Edge(v1, v3, 4)
# e3 = Edge(v1, v4, 3)
# e4 = Edge(v3, v4, 5)
# e5 = Edge(v2, v4, 2)
#
# e6 = Edge(v2, v1, 1)
# e7 = Edge(v3, v1, 4)
# e8 = Edge(v4, v1, 3)
# e9 = Edge(v4, v3, 5)
# e10 = Edge(v4, v2, 2)
#
# v1.add_out_edge(e1)
# v1.add_out_edge(e2)
# v1.add_out_edge(e3)
# v3.add_out_edge(e4)
# v2.add_out_edge(e5)
#
# v2.add_out_edge(e6)
# v3.add_out_edge(e7)
# v4.add_out_edge(e8)
# v4.add_out_edge(e9)
# v4.add_out_edge(e10)

p = Prims()
# p.add_vertex(v1)
# p.add_vertex(v2)
# p.add_vertex(v3)
# p.add_vertex(v4)
p.read_file('edges.txt')
print(p.find_min_spanning_tree())
