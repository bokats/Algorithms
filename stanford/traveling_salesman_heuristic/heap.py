import numpy as np

class MinHeap(object):
    def __init__(self):
        self.store = []

    def insert(self, start_city, edges):
        for edge in edges:
            self.store.append(edges[i])
            self.heapify_up()

    def extract_min(self):
        self.store[0], self.store[-1] = self.store[-1], self.store[0]
        min_edge = self.store.pop()
        self.heapify_down()
        return min_edge

    def heapify_up(self):
        new_edge_idx = len(self.store) - 1
        parent_idx = int((new_edge_idx - 1) / 2)
        while new_edge_idx != 0 and \
            self.store[new_edge_idx][2] < self.store[parent_idx][2]:
            self.store[new_edge_idx], self.store[parent_idx] = \
            self.store[parent_idx], self.store[new_edge_idx]
            new_edge_idx = parent_idx
            parent_idx = int((new_edge_idx - 1) / 2)

    def heapify_down(self):
        current_edge_idx = 0
        swap = True
        while swap:
            swap = False
            children = self.children_indeces(current_edge_idx)
            swap_idx = current_edge_idx
            for child_idx in children:
                if self.store[child_idx][2] < self.store[swap_idx][2]:
                    swap_idx = child_idx
                    swap = True
            if swap:
                self.store[current_edge_idx], self.store[swap_idx] = \
                self.store[swap_idx], self.store[current_edge_idx]
                current_edge_idx = swap_idx
        return self.store

    def children_indeces(self, parent_idx):
        result = []
        length = len(self.store)
        left = (2 * parent_idx) + 1
        right = (2 * parent_idx) + 2
        if left < length:
            result.append(left)
            if right < length:
                result.append(right)
        return result

# Tests

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
#
# h = MinHeap()
# h.insert(n4)
# assert len(h.get_store()) == 1
# h.insert(n3)
# h.insert(n2)
# h.insert(n1)
# assert len(h.get_store()) == 4
# assert h.get_store()[0] == n1
# assert h.extract_min() == n1
# assert len(h.get_store()) == 3
# assert h.extract_min() == n2
# assert len(h.get_store()) == 2
# assert h.extract_min() == n3
# assert len(h.get_store()) == 1
