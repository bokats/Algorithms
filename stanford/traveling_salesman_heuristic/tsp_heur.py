from math import inf
# from heap import MinHeap, Node
import random

class TSPHeuristic(object):
    def __init__(self):
        self.edges = None
        self.number_of_cities
        self.cities = None
        self.visited = set([])
        self.run_tsp(filename)

    def run_tsp(self, filename):
        self.read_file(filename)
        self.find_min_spanning_tree()

    def read_file(self, filename):
        f = open(filename, 'r')
        for line in f:
            line = line.split(" ")
            if len(city) < 2:
                self.number_of_cities = int(line[0])
                self.cities = np.zeros((self.number_of_cities + 1, 2))
            else:
                for i in range(len(line)):
                    line[i] = int(line[i])
                self.cities[line[0]] = [line[1], line[2]]
        f.close()

    def calculate_distance(self,coord1, coord2):
        return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

    def find_edges(self,city):
        edges = []
        for i in range(1, len(self.cities)):
            if i != city and i not in self.visited:
                distance = self.calculate_distance(self.coordinates[city], self.coordinates[i])
                edges.append([i, distance])

        return edges

    def find_min_spanning_tree(self):
        total_distance = 0
        self.visited.add(1)
        heap = MinHeap()

        for edge in self.find_edges(1,visited):
            heap.insert(edge)

        while len(visited) < len(self.number_of_cities):

            while True:
                min_edge = heap.extract_min()
                min_cost = min_edge[1]
                if min_edge[1] not in visited:
                    break

            total_distance += min_cost
            visited.add(min_edge[0])
            new_city = min_edge[0]

            for edge in self.find_edges(new_city):
                heap.insert(edge)

        return (total_distance, new_city)

p = Prims()
p.read_file('nn.txt')
