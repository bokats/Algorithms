import numpy as np

class TwoSat(object):
    def __init__(self,filename):
        self.vertices = set([])
        self.edges = {}
        self.explored = set([])
        self.s = None
        self.time = 0
        self.finishing_time = {}
        self.leader = {}
        self.actual_to_proxy = None
        self.proxy_to_actual = None
        self.run_two_sat(filename)

    def run_two_sat(self,filename):
        self.read_file(filename)
        self.DFS_loop()
        self.get_referenced_nodes()
        self.reverse_edges()
        self.reset_variables()
        self.DFS_loop()
        self.check_sat()

    def read_file(self,filename):
        f = open(filename, 'r')
        for line in f:
            line = line.split()
            if len(line) > 1:
                for i in range(len(line)):
                    line[i] = int(line[i])

                self.add_vertices(line[0], line[1])
                self.add_edges(line[0], line[1])

        self.vertices = list(self.vertices)
        self.vertices.sort(reverse=True)
        f.close()

    def add_edges(self, start_vertex, dest_vertex):
        if -start_vertex not in self.edges.keys():
            self.edges[-start_vertex] = [dest_vertex]
        else:
            self.edges[-start_vertex].append(dest_vertex)

        if -dest_vertex not in self.edges.keys():
            self.edges[-dest_vertex] = [start_vertex]
        else:
            self.edges[-dest_vertex].append(start_vertex)

    def add_vertices(self, start_vertex, dest_vertex):
        self.vertices.add(start_vertex)
        self.vertices.add(-start_vertex)
        self.vertices.add(dest_vertex)
        self.vertices.add(-dest_vertex)

    def reset_variables(self):
        self.explored = set([])
        self.s = None
        self.time = 0
        self.finishing_time = {}
        self.leader = {}

    def get_referenced_nodes(self):
        self.actual_to_proxy = self.finishing_time;
        self.proxy_to_actual = np.zeros(len(self.finishing_time.keys()) + 1, int)
        for vertex in self.finishing_time.keys():
            self.proxy_to_actual[self.finishing_time[vertex]] = vertex

    def DFS_loop(self):

        for vertex in self.vertices:
            if vertex not in self.explored:
                self.s = vertex
                self.DFS(vertex)

    def DFS(self, vertex):
        stack = [vertex]

        while len(stack) > 0:
            vertex = stack[-1]
            self.explored.add(vertex)
            self.leader[vertex] = self.s
            children = []

            if vertex in self.edges.keys():
                children = self.edges[vertex]

            count = 0
            for dest_vertex in children:
                if dest_vertex not in self.explored:
                    stack.append(dest_vertex)
                    break
                else:
                    count += 1

            if count == len(children):
                self.time += 1
                self.finishing_time[vertex] = self.time
                stack.pop()

    def reverse_edges(self):
        reversed_edges = {}
        for start_vertex in self.edges.keys():
            for dest_vertex in self.edges[start_vertex]:
                if self.finishing_time[dest_vertex] not in reversed_edges.keys():
                    reversed_edges[self.finishing_time[dest_vertex]] = \
                    [self.finishing_time[start_vertex]]
                else:
                    reversed_edges[self.finishing_time[dest_vertex]].\
                    append(self.finishing_time[start_vertex])

        self.vertices = [num for num in range(len(self.vertices), 0,-1)]
        self.edges = reversed_edges

    def check_sat(self):
        for vertex in self.vertices:
            if self.proxy_to_actual[vertex] > 0 and self.leader[vertex] == \
            self.leader[self.actual_to_proxy[-self.proxy_to_actual[vertex]]]:
                print("Unsatisfiable", 0)
                return
        print("Satisfiable", 1)

for i in range(1,7):
    filename = './txt_files/2sat' + str(i) + '.txt'
    TwoSat(filename)
