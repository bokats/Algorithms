from scipy import spatial
import numpy as np
from heap import MinHeap
from math import sqrt

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
                # if line[0] == '5001':
                #     break
                for i in range(1, len(line)):
                    line[i] = float(line[i])
                self.cities[int(line[0])] = [line[1], line[2]]

        for i in range(1, self.number_of_cities + 1):
            self.city_visits[i] = 0

        self.city_visits[1] = 1

        self.kd_tree = spatial.KDTree(self.cities[1:])
        f.close()

    def run_tsp(self,filename):
        self.read_file(filename)
        last_city, distance = self.prims_min_spanning_tree()
        self.connect_last_to_first(last_city, distance)

    def prims_min_spanning_tree(self):
        total_distance = 0.0
        self.visited.add(1)

        self.query_kd_tree(1)

        while len(self.visited) < self.number_of_cities:
            print(len(self.visited))
            while True:
                min_edge = self.heap.extract_min()
                # import pdb; pdb.set_trace()
                if min_edge[1] not in self.visited and \
                self.city_visits[min_edge[0]] < 2 and \
                self.city_visits[min_edge[1]] < 2:
                    break
                else:
                    self.kth_city[min_edge[0]] += 1
                    self.add_correct_edge(min_edge[0])
                    # self.query_kd_tree(min_edge[0])

            self.city_visits[min_edge[0]] += 1
            self.city_visits[min_edge[1]] += 1
            total_distance += min_edge[2]
            self.visited.add(min_edge[1])

            self.kth_city[min_edge[0]] += 1
            for i in range(2):
                self.add_correct_edge(min_edge[i])


        print(total_distance)
        return (min_edge[1], total_distance)

    def query_kd_tree(self, start_city):
        if self.city_visits[start_city] > 1:
            return
        kd_result = self.kd_tree.query(self.cities[start_city], self.kth_city[start_city])
        # import pdb; pdb.set_trace()
        distance, new_city = kd_result[0][-1], kd_result[1][-1]
        self.heap.insert([start_city, new_city + 1, distance])

    def calculate_distance(self,coord1, coord2):
        return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

    def connect_last_to_first(self, last, current_distance):
        edge_distance = self.calculate_distance(self.cities[1], self.cities[last])
        print(current_distance + edge_distance)

    def add_correct_edge(self,start_city):
        if self.city_visits[start_city] > 1:
            return
        result = self.kd_tree.query(self.cities[start_city], self.number_of_cities)
        all_results = self.kd_tree.query(self.cities[start_city], self.number_of_cities)
        for i in range(self.kth_city[start_city] - 1,len(all_results[0])):
            city = all_results[1][i] + 1
            if city not in self.visited and self.city_visits[city] < 2:
                self.heap.insert([start_city, city, all_results[0][i]])
                # import pdb; pdb.set_trace()
                return
            self.kth_city[start_city] += 1

t = TSPHeuristic("nn.txt")
