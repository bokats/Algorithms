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

    def read_file(self,filename):
        file = open(filename, 'r')
        count = 0
        for line in file:
            line = line.split()
            for i in range(len(line)):
                line[i] = int(line[i])
            if len(line) < 3:

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

        print(self.edges[47977])
        print(count)

bf = BellmanFord()
bf.read_file('g1.txt')
