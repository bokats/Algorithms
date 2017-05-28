import numpy as np

class UnionFind(object):
    def __init__(self, size):
        self.vertices = np.zeros(size, int)
        self.leaders = {}

    def add_vertex(self, key):
        self.vertices[key] = key
        self.leaders[key] = [key]

    def find_leader(self,key):
        return self.vertices[key]

    def union(self,leader_one,leader_two):
        if len(self.leaders[leader_one]) < len(self.leaders[leader_two]):
            self.merge_components(leader_two, leader_one)
        else:
            self.merge_components(leader_one, leader_two)

    def merge_components(self, larger_leader_key, smaller_leader_key):
        for key in self.leaders[smaller_leader_key]:
            self.vertices[key] = larger_leader_key
            self.leaders[larger_leader_key].append(key)
        del self.leaders[smaller_leader_key]
