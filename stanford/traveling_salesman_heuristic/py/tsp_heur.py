from math import inf, sqrt
from heap import MinHeap
import random
import numpy as np

class TSPHeuristic(object):
    def __init__(self, filename):
        self.edges = None
        self.number_of_cities = 0
        self.cities = None
        self.visited = set([])
        self.city_visits = {}
        self.run_tsp(filename)

    def run_tsp(self, filename):
        self.read_file(filename)
        distance, last = self.find_min_spanning_tree()
        self.connect_last_to_first(last, distance)

    def read_file(self, filename):
        f = open(filename, 'r')
        for line in f:
            line = line.split(" ")
            if len(line) < 2:
                self.number_of_cities = int(line[0])
                self.cities = np.zeros((self.number_of_cities + 1, 2))
            else:
                for i in range(1, len(line)):
                    line[i] = float(line[i])
                self.cities[int(line[0])] = [line[1], line[2]]

        for i in range(1, self.number_of_cities + 1):
            self.city_visits[i] = 0

        f.close()

    def calculate_distance(self,coord1, coord2):
        return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

    def find_edges(self,city):
        edges = []
        for i in range(1, len(self.cities)):
            if i != city and i not in self.visited and \
            self.city_visits[city] < 2 and self.city_visits[i] < 2:
                distance = self.calculate_distance(self.cities[city], self.cities[i])
                edges.append([city, i, distance])
        return edges

    def find_min_spanning_tree(self):
        total_distance = 0
        self.visited.add(1)
        heap = MinHeap()

        for edge in self.find_edges(1):
            heap.insert(edge)

        while len(self.visited) < self.number_of_cities:
            
            while True:
                min_edge = heap.extract_min()
                min_cost = min_edge[2]
                if min_edge[1] not in self.visited and \
                self.city_visits[min_edge[0]] < 2 and \
                self.city_visits[min_edge[1]] < 2:
                    break

            self.city_visits[min_edge[0]] += 1
            self.city_visits[min_edge[1]] += 1

            total_distance += min_cost
            self.visited.add(min_edge[1])
            new_city = min_edge[1]

            for edge in self.find_edges(min_edge[1]):
                heap.insert(edge)
        return (total_distance, min_edge[1])

    def connect_last_to_first(self, last, current_distance):
        edge_distance = self.calculate_distance(self.cities[1], self.cities[last])
        print(current_distance + edge_distance)

TSPHeuristic('nn.txt')

# print(t.find_edges(1))
