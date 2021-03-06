import numpy as np
from heap import MinHeap

class Johnson(object):
    def __init__(self):
        self.edges = None
        self.number_of_edges = 0
        self.number_of_vertices = 0
        self.distances = None
        self.out_edges = {}

    def read_file(self, filename):
        file = open(filename, 'r')
        count = 0
        for line in file:
            line = line.split()
            for i in range(len(line)):
                line[i] = int(line[i])
            if len(line) < 3:
                self.number_of_edges = line[1]
                self.number_of_vertices = line[0]
                self.edges = np.zeros((line[1], 3), int)
            else:
                self.edges[count] = line
                if line[0] in self.out_edges.keys():
                    self.out_edges[line[0]] = np.append(self.out_edges[line[0]], [count])
                else:
                    self.out_edges[line[0]] = np.array([count], int)
                count += 1

    def find_shortest_distance(self):
        shortest = 2147483647
        for v in range(1, self.number_of_vertices):
            sub_result = self.bellman_ford(v)
            if sub_result is None:
                return None
            if sub_result < shortest:
                shortest = sub_result
        return shortest

    def bellman_ford(self, start_vertex):
        self.distances = np.full(self.number_of_vertices + 1, 2147483647, int)
        self.distances[start_vertex] = 0

        for v in range(self.number_of_vertices - 1):
            changes = 0
            for i in range(self.number_of_edges):
                edge = self.edges[i]
                if self.distances[edge[0]] != 2147483647 and self.distances[edge[0]] + edge[2] < self.distances[edge[1]]:
                    self.distances[edge[1]] = self.distances[edge[0]] + edge[2]
                    changes += 1
            if changes == 0:
                return min(self.distances)

        for i in range(self.number_of_edges):
            edge = self.edges[i]
            if self.distances[edge[0]] != 2147483647 and self.distances[edge[0]] + edge[2] < self.distances[edge[1]]:
                print('Negative cycle')
                return None

        return min(self.distances)

    def create_dummy_node(self):
        new_edges = np.zeros((self.number_of_vertices, 3), int)
        new_vertex = self.number_of_vertices + 1

        for i in range(self.number_of_vertices):
            new_edges[i] = [new_vertex, i + 1, 0]

        self.edges = np.concatenate((self.edges, new_edges))
        self.number_of_edges += self.number_of_vertices
        self.number_of_vertices += 1

    def reweight_edges(self):

        for i in range(self.number_of_edges - self.number_of_vertices + 1):
            edge = self.edges[i]
            self.edges[i] = [edge[0], edge[1], edge[2] + self.distances[edge[0]] - self.distances[edge[1]]]

    def dijkstra(self,start_vertex):
        distances = np.full(self.number_of_vertices, 2147483647, int)
        visited = set([start_vertex])
        current_vertex = start_vertex
        heap = MinHeap()

        if current_vertex in self.out_edges.keys():
            for edge_idx in self.out_edges[current_vertex]:
                edge = self.edges[edge_idx]
                heap.insert([edge[2], edge[0], edge[1]])

        while not heap.empty():

            while True:
                if heap.empty():
                    min_edge = None
                    break
                else:
                    min_edge = heap.extract_min()
                    if min_edge[2] not in visited:
                        break

            if min_edge is None:
                break

            current_vertex = min_edge[2]
            distances[current_vertex] = min_edge[0]
            visited.add(current_vertex)

            if current_vertex in self.out_edges.keys():
                for edge_idx in self.out_edges[current_vertex]:
                    edge = self.edges[edge_idx]
                    if edge[1] not in visited:
                        heap.insert([distances[current_vertex] + edge[2], edge[0], edge[1]])

        shortest_distance = min(distances)
        min_distances = np.where(distances == shortest_distance)[0]
        result = 2147483647
        for i in min_distances:
            if shortest_distance + self.distances[i] - self.distances[start_vertex] < result:
                result = shortest_distance + self.distances[i] - self.distances[start_vertex]

        return result

    def johnson(self):
        self.create_dummy_node()
        bf = self.bellman_ford(self.number_of_vertices)
        if bf is None:
            return None
        else:
            self.reweight_edges()
            shortest_shortest_distance = 2147483647
            for v in range(1, self.number_of_vertices):
                d_result = self.dijkstra(v)
                if d_result < shortest_shortest_distance:
                    shortest_shortest_distance = d_result

        return shortest_shortest_distance

j = Johnson()
j.read_file('g3.txt')
print(j.johnson())
