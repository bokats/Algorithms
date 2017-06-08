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
        self.distances = None
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
                self.distances = np.zeros(line[0] + 1, float)
            else:
                self.edges[count] = line
                if line[1] in self.in_edges.keys():
                    self.in_edges[line[1]] = np.append(self.in_edges[line[1]], [count])
                else:
                    self.in_edges[line[1]] = np.array([count], int)
                count += 1

        for i in range(len(self.distances)):
            self.distances[i] = math.inf


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

        print(self.edges[self.number_of_edges])
        print(self.edges[self.number_of_edges - 1])
        print(self.edges[self.number_of_edges + 1])
        print(self.edges[self.number_of_edges + 1000 -1])

bf = BellmanFord()
bf.read_file('g1.txt')
bf.set_up_dummy_start_vertex()
