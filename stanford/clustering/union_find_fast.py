import numpy as np

class UnionFind(object):
    def __init__(self, size):
        self.vertices = [[None for x in range(2)] for x in range(size)]
        self.leaders = {}

    def add_vertex(self, key, binary):
        self.vertices[key] = [binary, key]
        self.leaders[key] = [key]

    def find_leader(self,key):
        return self.vertices[key][1]

    def union(self,leader_one,leader_two):
        if len(self.leaders[leader_one]) < len(self.leaders[leader_two]):
            self.merge_components(leader_two, leader_one)
        else:
            self.merge_components(leader_one, leader_two)

    def merge_components(self, larger_leader_key, smaller_leader_key):
        for key in self.leaders[smaller_leader_key]:
            self.vertices[key][1] = larger_leader_key
            self.leaders[larger_leader_key].append(key)
        del self.leaders[smaller_leader_key]
