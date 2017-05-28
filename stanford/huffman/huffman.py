from heap import MinHeap

class Node(object):
    def __init__(self,key,value,left,right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.binary = None

class Huffman(object):
    def __init__(self):
        self.heap = MinHeap()

    def read_file(self, filename):
        file = open(filename, 'r')
        count = 0
        for line in file:
            if count != 0:
                line = int(line)
                node = Node(str(count),line, None, None)
                self.heap.insert(node)
                count += 1

    def build_tree(self):

        while len(self.heap.store) > 1:
            min_two = []
            for _ in range(2):
                min_two.append(self.heap.extract_min())
            self.merge_nodes(min_two[0], min_two[1])

        self.assign_binary(self.heap.extract_min())

    def merge_nodes(self, node1, node2):
        new_node = Node(node1.key + node2.key, node1.value + node2.value, node1, node2)
        self.heap.insert(new_node)

    def assign_binary(self, root):
        stack = [root]
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
                current_node.right.binary = 1
            if current_node.left:
                stack.append(current_node.left)
                current_node.left.binary = 0

        
h = Huffman()
h.read_file('huffman.txt')
h.build_tree()
