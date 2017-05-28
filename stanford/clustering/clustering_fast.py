from union_find_fast import UnionFind
import numpy as np

class ClusteringMST(object):
    def __init__(self):
        self.union_find = UnionFind(200000)
        self.vertices = {}

    # def hamming_distance(self, n1, n2):

    def read_file(self, filename):
        file = open(filename, 'r')
        count = 0
        for line in file:
            line = line.replace(" ", "")
            if len(line) > 10:
                self.union_find.add_vertex(count)
                if line in self.vertices.keys():
                    self.vertices[line].append(count)
                else:
                    self.vertices[line] = [count]
                count += 1

    def find_k_clustering(self, k):



        return len(self.union_find.leaders)

    def generate_hamming_distances(self, binary):
        binary = [el for el in binary]
        zero_diff = [''.join(binary)]
        one_diff = []
        two_diff = []
        binary_copy = binary[:]

        for i in range(len(binary)):
            if binary[i] == '1':
                binary[i] = '0'
            else:
                binary[i] = '1'
            one_diff.append(''.join(binary))
            binary = binary_copy[:]

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
                two_diff.append(''.join(binary))
                j += 1
                binary = binary_copy[:]

        return zero_diff, one_diff, two_diff

c = ClusteringMST()
print(c.generate_hamming_distances('111111111111111111111111'))
c.read_file('clustering_big.txt')
# print(c.find_k_clustering(3))
