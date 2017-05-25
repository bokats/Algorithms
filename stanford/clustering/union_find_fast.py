import numpy as np

class UnionFind(object):
    def __init__(self, size):
        self.vertices = np.zeros((size,2), int)
        self.leaders = {}

    def add_vertex(self, vertex, leader = None):
        if vertex.key not in self.vertices.keys():
            if leader:
                vertex.leader = leader
                self.leaders[leader.key].append(vertex.key)
            elif vertex.leader.key in self.leaders.keys():
                self.leaders[vertex.leader.key].append(vertex.key)
            else:
                self.leaders[vertex.leader.key] = [vertex.key]
            self.vertices[vertex.key] = vertex

    def find(self,vertex):
        return self.vertices[vertex - 1][1]

    def union(self,leader_one,leader_two):
        if len(self.leaders[leader_one]) < len(self.leaders[leader_two]):
            self.merge_components(leader_two, leader_one)
        else:
            self.merge_components(leader_one, leader_two)

    def merge_components(self, larger_leader_key, smaller_leader_key):
        for key in self.leaders[smaller_leader_key]:
            self.vertices[key - 1][1] = larger_leader_key
            self.leaders[larger_leader_key].append(key)
        self.vertices[smaller_leader_key - 1][1] = larger_leader_key
        self.leaders[larger_leader_key].append(smaller_leader_key)
        del self.leaders[smaller_leader_key]
