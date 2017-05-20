from vertex import Vertex, Edge
from math import inf
from heap import MinHeap, Node
from random import choice

class Prims(object):
    def __init__(self):
        self.vertices = {}

    def read_file(self, filename):
        file = open(filename, 'r')
        for line in file:
            edge = line.split(" ")
            for num in edge:
                num = int(num)

            if len(edge) > 2:
                if edge[0] not in self.vertices.keys():
                    self.vertices[edge[0]] = Vertex(edge[0])
                if edge[1] not in self.vertices.keys():
                    self.vertices[edge[1]] = Vertex(edge[1])
                new_edge = Edge(self.vertices[edge[0]], self.vertices[edge[1]], edge[2])
                self.vertices[edge[0]].add_out_edge(new_edge)

    def find_min_spanning_tree(self):
        result = 0
        current_vertex = random.choice(self.vertices.keys())
        visited = set([current_vertex.key])
        heap = MinHeap()

        for edge in current_vertex.out_edges:
            heap.insert(Node(edge.cost, edge))

        while len(visited) != len(self.vertices):

            while True:
                min_node = heap.extract_min()
                min_edge = min_node.edge
                min_cost = min_node.cost
                if min_edge.end_vertex.key not in visited:
                    break

            result += min_cost
            visited.add(min_edge.end_vertex.key)
            current_vertex = min_edge.end_vertex

            for edge in current_vertex.out_edges:
                if edge.end_vertex not in visited:
                    heap.insert(Node(edge.cost, edge))

        return result
