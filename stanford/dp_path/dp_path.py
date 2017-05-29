class MaxPath(object):
    def __init__(self):
        self.vertices = []

    def read_file(self, filename):
        file = open(filename, 'r')
        count = 0
        for line in file:
            if count != 0:
                self.vertices.append(int(line))
            count += 1

    def find_max_weight(self, test_vertices):
        table = [0, self.vertices[0]]

        for i in range(1, len(self.vertices)):
            table.append(max(table[-1], table[-2] + self.vertices[i]))

        path = set([])

        idx = len(table) - 1
        while idx >= 1:
            if table[idx - 1] >= table[idx - 2] + self.vertices[idx - 1]:
                idx -= 1
            else:
                path.add(idx)
                idx -= 2

        result = ""
        for v in test_vertices:
            if v in path:
                result += '1'
            else:
                result += '0'
        return result

m = MaxPath()
m.read_file('dp_path.txt')

print(m.find_max_weight([1,2,3,4,17,117,517,997]))
# print(m.find_max_weight([1, 3, 6, 9]))
