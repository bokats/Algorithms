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

    def find(self,vertex_key):
        return self.vertices[vertex_key].leader

    def union(self,leader_one_key,leader_two_key):
        if len(self.leaders[leader_one_key]) < len(self.leaders[leader_two_key]):
            self.merge_components(leader_two_key, leader_one_key)
        else:
            self.merge_components(leader_one_key, leader_two_key)

    def merge_components(self, larger_leader_key, smaller_leader_key):
        for key in self.leaders[smaller_leader_key]:
            self.vertices[key].leader = self.vertices[larger_leader_key]
            self.leaders[larger_leader_key].append(key)
        self.vertices[smaller_leader_key].leader = self.vertices[larger_leader_key]
        self.leaders[larger_leader_key].append(smaller_leader_key)
        del self.leaders[smaller_leader_key]
