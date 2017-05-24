class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.leader = self

class Edge(object):
    def __init__(self, vertex_one, vertex_two, cost):
        self.vertex_one = vertex_one
        self.vertex_two = vertex_two
        self.cost = cost

class UnionFind(object):
    def __init__(self):
        self.vertices = {}
        self.leaders = {}

    def find(self,vertex_key):
        return self.vertices[vertex_key].leader

    def union(self,leader_one_key,leader_two_key):
        if len(self.leaders[leader_one]) > len(self.leaders[leader_two]):
            merge_components(leader_one_key, leader_two_key)
        else:
            merge_components(leader_two_key, leader_one_key)
        
    def merge_components(self, larger_leader_key, smaller_leader_key):
        for key in self.leaders[smaller_leader_key]:
            self.vertices[key].leader = self.vertices[larger_leader_key]
            self.leaders[larger_leader_key].append(key)
        self.vertices[smaller_leader_key].leader = self.vertices[larger_leader_key]
        self.leaders[larger_leader_key].append(smaller_leader_key)
        del self.leaders[smaller_leader_key]
