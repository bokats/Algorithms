from union_find_fast import UnionFind
import numpy as np

class ClusteringMST(object):
    def __init__(self):
        self.union_find = UnionFind(200000)

    def hamming_distance(self, n1, n2):
        return bin(n1^n2).count('1')

    def read_file(self, filename):
        file = open(filename, 'r')
        count = 0
        for line in file:
            line = line.replace(" ", "")
            if len(line) > 10:
                self.union_find.add_vertex(int(line, 2), count)
                count += 1

    def find_k_clustering(self, k):

        for i in range(len(self.union_find.vertices)):
            j = i + 1
            print(i)
            while j < len(self.union_find.vertices):
                dis = self.hamming_distance(self.union_find.vertices[i][0], self.union_find.vertices[j][0])
                if dis < k + 1 and self.union_find.find(i) != self.union_find.find(j):
                    self.union_find.union(i, j)
                j += 1

        return len(self.union_find.leaders)

    def generate_hamming_distances(self, binary):
        zero_diff = [binary]
        one_diff = []
        two_diff = []
        binary_copy = binary

        for i in range(len(binary)):
            if i == '1':
                binary[i] = '0'
            else:
                binary[i] = '1'
            one_diff.append(binary)
            binary = binary_copy

        for i in range(len(binary) - 1):
            zero = True
            if binary[i] == '1':
                zero = False
            j = i + 1
            while j < len(binary):
                if zero:
                    binary[i] = '1'
                else:
                    binary[i] = '0'
                if binary[j] == '0':
                    binary[j] = '1'
                else:
                    binary[j] = '0'
                two_diff.append(binary)
                j += 1
                binary = binary_copy

        print(len(two_diff))
        
c = ClusteringMST()
c.generate_hamming_distances('111111111111111111111111')

c.read_file('clustering_big.txt')
print(c.find_k_clustering(3))
