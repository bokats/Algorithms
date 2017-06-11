import numpy as np

class BellmanFord(object):
    def __init__(self):
        self.edges = None
        self.in_edges = {}
        self.number_of_edges = 0
        self.number_of_vertices = 0

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
        distances = np.full(self.number_of_vertices + 1, 2147483647, int)
        distances[start_vertex] = 0

        for v in range(self.number_of_vertices - 1):
            changes = 0
            print(v)
            for i in range(self.number_of_edges):
                edge = self.edges[i]
                if distances[edge[0]] != 2147483647 and distances[edge[0]] + edge[2] < distances[edge[1]]:
                    distances[edge[1]] = distances[edge[0]] + edge[2]
                    changes += 1
            if changes == 0:
                return min(distances)

        for i in range(self.number_of_edges):
            edge = self.edges[i]
            if distances[edge[0]] != 2147483647 and distances[edge[0]] + edge[2] < distances[edge[1]]:
                print('Negative cycle')
                return None

        return min(distances)

bf = BellmanFord()
bf.read_file('g1.txt')
# print(bf.bellman_ford(1))
print(bf.find_shortest_distance())
