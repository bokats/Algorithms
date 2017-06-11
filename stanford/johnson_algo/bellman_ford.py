import numpy as np

class Johnson(object):
    def __init__(self):
        self.edges = None
        self.number_of_edges = 0
        self.number_of_vertices = 0
        self.distances = None

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
        self.bellman_ford(self.number_of_vertices)

    def reweight_edges(self):

        for i in range(self.number_of_edges - self.number_of_vertices + 1):
            edge = self.edges[i]
            self.edges[i] = [edge[0], edge[1], edge[2] + self.distances[edge[0]] - self.distances[edge[1]]]

j = Johnson()
j.read_file('test1.txt')
j.create_dummy_node()
j.reweight_edges()
# print(bf.bellman_ford(1))
# print(bf.find_shortest_distance())
