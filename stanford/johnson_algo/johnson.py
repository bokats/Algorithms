import numpy as np
from heap import MinHeap

class Johnson(object):
    def __init__(self):
        self.edges = None
        self.in_edges = {}
        self.out_edges = {}
        self.number_of_edges = 0
        self.number_of_vertices = 0
        self.distances = None

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
            new_row = np.zeros(self.number_of_vertices + 2)
            for j in range(1, len(new_row) - 1):
                min_distance = np.inf
                for edge_idx in self.in_edges[j]:
                    edge = self.edges[edge_idx]
                    if prev_row[edge[0]] != np.inf and prev_row[edge[0]] + edge[2] < min_distance:
                        min_distance = prev_row[edge[0]] + edge[2]
                new_row[j] = min(prev_row[j], min_distance)
            prev_row = np.copy(new_row)

        self.distances = np.copy(prev_row)

    def check_for_cycles(self):
        for vertex in range(1, len(self.distances) - 1):
            min_distance = np.inf
            for edge_idx in self.in_edges[vertex]:
                edge = self.edges[edge_idx]
                if self.distances[edge[0]] != np.inf and self.distances[edge[0]] + edge[2] < min_distance:
                    min_distance = self.distances[edge[0]] + edge[2]
            if min(self.distances[vertex], min_distance) != self.distances[vertex]:
                return True

        return False

    def reweight_edges(self):
        for i in range(self.number_of_edges):
            edge = self.edges[i]
            edge[2] = edge[2] - self.distances[edge[1]] + self.distances[edge[0]]
            self.edges[i] = edge

        print(self.edges)

    def run_dijksta(self):
        for i in range(self.number_of_edges):
            edge = self.edges[i]
            if edge[0] in self.out_edges.keys():
                self.out_edges[edge[0]] = np.append(self.out_edges[edge[0]], [i])
            else:
                self.out_edges[edge[0]] = np.array([i], int)


        shortest_distance = np.inf
        shortest_path = []

        for vertex in range(1, self.number_of_vertices + 1):
            shortest = self.dijksra(vertex)
            if shortest[0] < shortest_distance:
                shortest_distance = shortest[0]
                shortest_path = [vertex, shortest[1]]

        return shortest_distance - self.distances[shortest_path[0]] + \
        self.distances[shortest_path[1]]

    def dijksra(self, start_vertex):

        shortest_distances = np.full(self.number_of_vertices + 1, np.inf)
        visited = set([start_vertex])
        current_vertex = start_vertex
        heap = MinHeap()

        if current_vertex in self.out_edges.keys():
            for edge_idx in self.out_edges[current_vertex]:
                edge = self.edges[edge_idx]
                heap.insert([edge[2], edge[0], edge[1]])

        while not heap.empty():

            while True:
                if heap.empty():
                    min_edge = None
                else:
                    min_edge = heap.extract_min()
                    if min_edge[2] not in visited:
                        break
                        
            import pdb; pdb.set_trace()
            if not min_edge:
                break

            current_vertex = min_edge[2]
            shortest_distances[current_vertex] = min_edge[0]
            visited.add(current_vertex)

            if current_vertex in self.out_edges.keys():
                for edge_idx in self.out_edges[current_vertex]:
                    edge = self.edges[edge_idx]
                    if edge[1] not in visited:
                        heap.insert([shortest_distances[current_vertex] + edge[2], edge[0], edge[1]])



        shortest_distances[start_vertex] = np.inf
        shortest_distance = np.inf
        shortest_end_vertex = None

        for i in range(len(shortest_distances)):
            if shortest_distances[i] < shortest_distance:
                shortest_distance = shortest_distances[i]
                shortest_end_vertex = i

        return [shortest_distance, shortest_end_vertex]

    def run_johnson(self, filename):

        self.read_file(filename)
        self.set_up_dummy_start_vertex()
        self.run_bellman_ford()
        if self.check_for_cycles():
            return None
        else:
            self.reweight_edges()
            return self.run_dijksta()

filenames = ['test4.txt']
shortest = np.inf
for filename in filenames:
    j = Johnson()
    result = j.run_johnson(filename)
    if result < shortest:
        shortest = result

print(result)
