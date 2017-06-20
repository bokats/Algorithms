import numpy as np
from math import sqrt
import itertools
import copy
import timeit

class TSP(object):
    def __init__(self):
        self.distances = None
        self.coordinates = None
        self.number_of_cities = 0

    def read_file(self, filename):
        file = open(filename, 'r')
        count = 0
        for line in file:
            line = line.split()
            if len(line) < 2:
                self.number_of_cities = int(line[0])
                self.coordinates = np.zeros((self.number_of_cities + 1, 2))
                self.distances = np.zeros((self.number_of_cities + 1, self.number_of_cities + 1))
            else:
                for i in range(len(line)):
                    line[i] = float(line[i])
                self.coordinates[count + 1] = line
                count += 1

    def calculate_distance(self, coordinates1, coordinates2):
        return sqrt((coordinates1[0] - coordinates2[0])**2 + (coordinates1[1] - coordinates2[1])**2)

    def solve_tsp_dp(self):
        for i in range(1, self.number_of_cities + 1):
            for j in range(1, self.number_of_cities + 1):
                self.distances[i][j] = self.calculate_distance(self.coordinates[i], self.coordinates[j])

        results = {}
        results[tuple([1])] = np.zeros(self.number_of_cities + 1)
        for m in range(2, self.number_of_cities + 1):
            print(m)
            start_time = timeit.default_timer()
            new_results = {}
            for C in itertools.combinations(range(1, self.number_of_cities + 1), m):
                if 1 not in C:
                    continue
                for j in C:
                    if j == 1:
                        new_results[C] = np.full(self.number_of_cities + 1, np.inf)
                    else:
                        minimum = np.inf
                        for k in C:
                            if k != j:
                                temp = list(C)
                                temp.remove(j)
                                if results[tuple(temp)][k] + self.distances[k][j] < minimum:
                                    minimum = results[tuple(temp)][k] + self.distances[k][j]
                        new_results[tuple(C)][j] = minimum
            results = copy.deepcopy(new_results)
            print(timeit.default_timer() - start_time)

        shortest_dis = np.inf
        for j in range(2, self.number_of_cities + 1):
            score = self.distances[j][1] + results[tuple(range(1, self.number_of_cities + 1))][j]
            if score < shortest_dis:
                shortest_dis = score

        return shortest_dis

    def find_distance(self,res):
        total = 0
        for i in range(len(res) - 1):
            j = i + 1
            total += self.distances[res[i]][res[j]]
        return total

tsp = TSP()
tsp.read_file('tsp.txt')
print(tsp.solve_tsp_dp())
