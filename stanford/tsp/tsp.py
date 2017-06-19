import numpy as np
from math import sqrt
import itertools

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
        for m in range(2, self.number_of_cities):
            for C in itertools.combinations(range(1, self.number_of_cities + 1), m):
                for j in C:
                    if j == 1:
                        results[tuple(C)] = np.zeros(len(C))
                    else:
                        for k in C:
                            minimum = np.inf
                            if k != j:
                                temp = C[:]
                                temp.remove(j)
                                if results[temp][k] + self.distances[k][j] < minimum:
                                    minumum = results[temp][k] + self.distances[k][j]
                        results[tuple(C)][j] = minimum
        



        # A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(self.distances[0][1:])}
        # for m in range(2, self.number_of_cities):
        #     print(m)
        #     B = {}
        #     for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, self.number_of_cities), m)]:
        #         for j in S - {0}:
        #             B[(S, j)] = min( [(A[(S-{j},k)][0] + self.distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
        #     A = B
        # res = min([(A[d][0] + self.distances[0][d[1]], A[d][1]) for d in iter(A)])
        # return res


    # def solve_tsp_dynamic(self):
    #     all_distances = [[length(x,y) for y in points] for x in points]
    #     #initial value - just distance from 0 to every other point + keep the track of edges
    #     A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
    #     cnt = len(points)
    #     for m in range(2, cnt):
    #         B = {}
    #         for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
    #             for j in S - {0}:
    #                 B[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j])  #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
    #         A = B
    #     res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    #     return res[1]

tsp = TSP()
tsp.read_file('test1.txt')
print(tsp.solve_tsp_dp())
