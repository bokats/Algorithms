import numpy as np
import math

class Vertex(object):
    def __init__(self):
        self.key = key
        self.in_edges = np.array([], int)
        self.distance = math.inf

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
            new_row = np.zeros(self.number_of_vertices + 2, int)
            for j in range(1, len(new_row)):
                min_distance = np.inf
                for edge in self.in_edges[j]:
                    if prev_row[edge[0]] != np.inf and prev_row[edge[0]] + edge[2] < min_distance:
                        min_distance = prev_row[edge[0]] + edge[2]
                new_row[j] = min(prev_row[j], min_distance)
                


bf = BellmanFord()
bf.read_file('g1.txt')
bf.set_up_dummy_start_vertex()
