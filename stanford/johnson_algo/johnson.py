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

        for line in file:
            line = line.split()
            for i in range(len(line)):
                line[i] = int(line[i])
            count = 0
            if len(line) < 3:
                self.edges = np.zeros((line[1], 3), int)
                self.distances = np.zeros(line[0] + 1, int)
            else:
                self.edges[count] = line
                if count in self.in_edges.keys():
                    
