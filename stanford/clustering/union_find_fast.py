import numpy as np

class UnionFind(object):
    def __init__(self, size):
        self.vertices = np.zeros((size, 2), int)
        self.leaders = {}

    def add_vertex(self, number, leader):
        self.vertices[leader] = [number, leader]
        self.leaders[leader] = np.array([leader])

    def find(self,vertex):
        return self.vertices[vertex][1]

    def union(self,leader_one,leader_two):
        if len(self.leaders[leader_one]) < len(self.leaders[leader_two]):
            self.merge_components(leader_two, leader_one)
        else:
            self.merge_components(leader_one, leader_two)

    def merge_components(self, larger_leader_key, smaller_leader_key):
        for key in self.leaders[smaller_leader_key]:
            self.vertices[key][1] = larger_leader_key
            np.append(self.leaders[larger_leader_key], [key])
        self.vertices[smaller_leader_key][1] = larger_leader_key
        np.append(self.leaders[larger_leader_key], [smaller_leader_key])
        del self.leaders[smaller_leader_key]
