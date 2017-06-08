import numpy as np
import math

class BellmanFord(object):
    def __init__(self):
        self.edges = None
        self.in_edges = {}
        self.number_of_edges = 0
        self.number_of_vertices = 0

    def read_file(self,filename):
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


    def set_up_dummy_start_vertex(self):
        new_edges = []
        for i in range(1, self.number_of_vertices + 1):
            new_edges.append([self.number_of_vertices + 1, i, 0])

        self.edges = np.concatenate((self.edges, new_edges))
        count = self.number_of_edges
        for i in range(count, len(self.edges)):
            edge = self.edges[i]
            if edge[1] in self.in_edges.keys():
                self.in_edges[edge[1]] = np.append(self.in_edges[edge[1]], [count])
            else:
                self.in_edges[edge[1]] = np.array([count], int)
            count += 1

    def run_bellman_ford(self):
        prev_row = np.full(self.number_of_vertices + 2, np.inf)

        prev_row[self.number_of_vertices + 1] = 0

        for _ in range(len(self.edges)):
            new_row = np.zeros(self.number_of_vertices + 2)
            for j in range(1, len(new_row) - 1):
                min_distance = np.inf
                for edge_idx in self.in_edges[j]:
                    edge = self.edges[edge_idx]
                    if prev_row[edge[0]] != np.inf and prev_row[edge[0]] + edge[2] < min_distance:
                        min_distance = prev_row[edge[0]] + edge[2]
                new_row[j] = min(prev_row[j], min_distance)
            prev_row = np.copy(new_row)
        self.reweight_edges(prev_row)

    def reweight_edges(self, distances):
        for i in range(self.number_of_edges):
            # import pdb; pdb.set_trace()
            edge = self.edges[i]
            edge[2] = edge[2] - distances[edge[1]] + distances[edge[0]]
            self.edges[i] = edge


bf = BellmanFord()
bf.read_file('test1.txt')
bf.set_up_dummy_start_vertex()
bf.run_bellman_ford()
