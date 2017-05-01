import os
from vertex import Vertex, Edge
from math import inf

file_name = "dijkstraData.txt"

class Dijkstra(object):
    def __init__(self, file_path):
        self.vertices = {}
        self.edges = {}
        self.convert_adj_list_to_graph(file_path)

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def find_shortest_distance(self, start_vertex_key, end_vertex_key):
        if start_vertex_key == end_vertex_key:
            return 0

        visited = set([self.vertices[start_vertex_key]])
        current_vertex = self.vertices[start_vertex_key]
        avail_edges = current_vertex.get_out_edges()

        while current_vertex.get_key() != end_vertex_key:
            min_distance = inf
            min_edge = None

            for edge in avail_edges:
                if edge.get_end_vertex() not in visited:
                    dis = edge.get_start_vertex().get_shortest_distance() + \
                    edge.get_distance()
                    if dis < min_distance:
                        min_distance = dis
                        min_edge = edge

            min_edge.get_end_vertex().set_shortest_distance(min_distance)
            min_edge.get_end_vertex().set_path(min_edge.get_start_vertex() \
                .get_path() + [min_edge.get_start_vertex().get_key()])
            current_vertex = min_edge.get_end_vertex()
            visited.add(current_vertex)

            for edge in current_vertex.get_out_edges():
                if edge.get_end_vertex() not in visited:
                    avail_edges.append(edge)

        return current_vertex.get_shortest_distance()

    def convert_adj_list_to_graph(self, file_path):
        file = open(file_path, "r")
        for line in file:
            line = line.split()
            for el in line:
                if "," not in el:
                    key = int(el)
                    start_key = key
                    if key not in self.vertices.keys():
                        self.vertices[key] = Vertex(key)
                else:
                    el = el.split(",")
                    key = int(el[0])
                    if key not in self.vertices.keys():
                        self.vertices[key] = Vertex(key)
                    new_edge = Edge(self.vertices[start_key], self.vertices[key], int(el[1]))
                    if key not in self.edges.keys():
                        self.edges[key] = [new_edge]
                    else:
                        self.edges[key].append(new_edge)
                    self.vertices[start_key].add_out_edge(new_edge)


# def djikstra(graph, start_node, end_node):

# Tests

d = Dijkstra(file_name)
# assert len(d.vertices[200].get_out_edges()) == 25
# assert len(d.vertices[1].get_out_edges()) == 27

print(7, d.find_shortest_distance(1, 7))

d = Dijkstra(file_name)
print(37, d.find_shortest_distance(1, 37))

d = Dijkstra(file_name)
print(59, d.find_shortest_distance(1, 59))

d = Dijkstra(file_name)
print(82, d.find_shortest_distance(1, 82))

d = Dijkstra(file_name)
print(99, d.find_shortest_distance(1, 99))

d = Dijkstra(file_name)
print(115, d.find_shortest_distance(1, 115))

d = Dijkstra(file_name)
print(133, d.find_shortest_distance(1, 133))

d = Dijkstra(file_name)
print(165, d.find_shortest_distance(1, 165))

d = Dijkstra(file_name)
print(188, d.find_shortest_distance(1, 188))

d = Dijkstra(file_name)
print(197, d.find_shortest_distance(1, 197))
