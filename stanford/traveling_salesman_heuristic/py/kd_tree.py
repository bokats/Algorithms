from scipy import spatial
import numpy as np
from heap import MinHeap

class TSPHeuristic(object):
    def __init__(self, filename):
        self.edges = None
        self.kd_tree = None
        self.city_visits = {}
        self.visited = set([])
        self.kth_city = None
        self.heap = MinHeap()
        self.run_tsp(filename)

    def read_file(self, filename):
        f = open(filename, 'r')
        for line in f:
            line = line.split(" ")
            if len(line) < 2:
                self.number_of_cities = int(line[0])
                self.cities = np.zeros((self.number_of_cities + 1, 2))
                self.kth_city = np.full(self.number_of_cities + 1, 2, dtype=np.int32)
            else:
                for i in range(1, len(line)):
                    line[i] = float(line[i])
                self.cities[int(line[0])] = [line[1], line[2]]

        for i in range(1, self.number_of_cities + 1):
            self.city_visits[i] = 0

        self.kd_tree = spatial.KDTree(self.cities[1:])
        f.close()

    def run_tsp(self,filename):
        self.read_file(filename)

    def prims_min_spanning_tree(self):
        total_distance = 0
        self.visited.add([1])

        self.query_kd_tree(1)

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

            self.kth_city[min_edge[0]] += 1
            self.query_kd_tree(min_edge[0])
            self.query_kr_tree(min_edge[1])




    def query_kd_tree(self, start_city):
        kd_result = self.kd_tree.query(self.cities[start_city], self.kth_city[start_city])
        distance, new_city = kd_result[0][-1], kd_result[1][-1]
        self.heap.insert([start_city, new_city, distance])
