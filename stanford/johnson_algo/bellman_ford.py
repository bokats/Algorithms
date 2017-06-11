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
                if line[1] in self.in_edges.keys():
                    self.in_edges[line[1]] = np.append(self.in_edges[line[1]], [count])
                else:
                    self.in_edges[line[1]] = np.array([count], int)
                count += 1

    def bellman_ford(self, start_vertex):
        prev_row = np.full(self.number_of_vertices + 1, 2147483647, int)
        prev_row[start_vertex] = 0

        for _ in range(self.number_of_edges):
            new_row = np.full(self.number_of_vertices + 1, 2147483647, int)
            for v in range(1, len(new_row)):
                if v in self.in_edges.keys():
                    min_distance = 2147483647
                    for edge_idx in self.in_edges[v]:
                        edge = self.edges[edge_idx]
                        if prev_row[edge[0]] != 2147483647 and prev_row[edge[0]] + edge[2] < min_distance:
                            min_distance = prev_row[edge[0]] + edge[2]
                    new_row[v] = min(prev_row[v], min_distance)
                else:
                    new_row[v] = prev_row[v]
            if np.array_equal(prev_row, new_row):
                break
            prev_row = np.copy(new_row)

        if self.check_for_cycles(prev_row):
            return None
        else:
            return new_row

    def check_for_cycles(self, prev_row):
        for v in range(1, len(prev_row)):
            if v in self.in_edges.keys():
                min_distance = 2147483647
                for edge_idx in self.in_edges[v]:
                    edge = self.edges[edge_idx]
                    if prev_row[edge[0]] != 2147483647 and prev_row[edge[0]] + edge[2] < min_distance:
                        min_distance = prev_row[edge[0]] + edge[2]
                if min(prev_row[v], min_distance) != prev_row[v]:
                    return True

        return False

bf = BellmanFord()
bf.read_file('test1.txt')
print(bf.bellman_ford(1))
