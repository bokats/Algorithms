
filename = "C:/Users/Bozhidar/Algorithms_stanford/PS4_SCC/SCC.txt"
def read_file():
    f = open(filename, "r")
    vertices = set([])
    dic = {}

    for line in f:

        line = line.split()

        vertices.add(int(line[0]))
        vertices.add(int(line[1]))

        if int(line[0]) not in dic.keys():
            dic[int(line[0])] = [(int(line[0]), int(line[1]))]
        else:
            dic[int(line[0])].append((int(line[0]), int(line[1])))

    return vertices, dic

vertices, edges = read_file()
print("Reading file: Done")

#vertices = [1,2,3,4,5,6,7,8,9]
#edges = {1: [(1,7)], 7: [(7,4), (7,9)], 4: [(4,1)], 9:[(9,6)], 6: [(6,3), (6,8)], 3: [(3,9)], 8: [(8,2)], 2: [(2,5)], 5: [(5,8)]}
#print(edges)

class Variables(object):
    def __init__(self):
        self.t = 0
        self.s = None
        self.explored = set([])
        self.leader = [None] * (len(vertices) + 1)
        self.f = [None] * (len(vertices) + 1)
        self.stack = []

    def get_t(self):
        return self.t

    def get_s(self):
        return self.s

    def get_explored(self):
        return self.explored

    def get_leader(self):
        return self.leader

    def get_f(self):
        return self.f

    def get_stack(self):
        return self.stack

variables = Variables()

def DFS_loop(vertices, dic):

    for i in range(len(vertices), 0, -1):
        if i not in variables.get_explored():
            variables.s = i
            DFS(vertices, dic, i)
#
def DFS(vertices, dic, i):

    variables.stack = [i]

    while len(variables.get_stack()) > 0:
        i = variables.get_stack()[-1]
        variables.explored.add(i)
        variables.leader[i] = variables.get_s()

        try:
            appl_edges = dic[i]
        except KeyError:
            appl_edges = []

        count = 0
        for edge in appl_edges:
            if edge[1] not in variables.explored:
                variables.stack.append(edge[1])
                break
            else:
                count += 1

        if count == len(appl_edges):
            variables.t += 1
            variables.f[i] = variables.get_t()
            variables.stack.pop(-1)

DFS_loop(vertices, edges)
print("First loop done")
#print(variables.get_f())

def reverse_edges(dic, f):
    reversed_edges = {}
    for key in dic.keys():
        for value in dic[key]:
            if f[value[1]] not in reversed_edges.keys():
                reversed_edges[f[value[1]]] = [(f[value[1]], f[key])]
            else:
                reversed_edges[f[value[1]]].append((f[value[1]], f[key]))

    return reversed_edges

reversed_dic = reverse_edges(edges, variables.get_f())
variables = Variables()

DFS_loop(vertices, reversed_dic)
print("Second loop done")

def get_largest_scc(leader):
    dic = {}
    scc = []

    for i in leader[1:]:
        try:
            dic[i] += 1
        except KeyError:
            dic[i] = 1

    for key in dic.keys():
        scc.append(dic[key])

    scc.sort(reverse = True)

    return scc[0:5]

print(get_largest_scc(variables.get_leader()))
