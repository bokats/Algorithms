class MinHeap(object):
    def __init__(self):
        self.store = []

    def insert(self, edge):
        self.store.append(edge)
        self.heapify_up()

    def empty(self):
        if self.store:
            return False
        else:
            return True

    def extract_min(self):
        self.store[0], self.store[-1] = self.store[-1], self.store[0]
        min_node = self.store.pop()
        self.heapify_down()
        return min_node

    def heapify_up(self):
        new_edge_idx = len(self.store) - 1
        parent_idx = int((new_edge_idx - 1) / 2)
        while new_edge_idx != 0 and \
            self.store[new_edge_idx][0] < self.store[parent_idx][0]:
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
                if self.store[child_idx][0] < self.store[swap_idx][0]:
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

h = MinHeap()
h.insert([2,1,1])
assert h.store == [[2,1,1]]
h.insert([0,4,3])
h.insert([1,5,2])
h.insert([3, 6, 8])
assert len(h.store) == 4
assert h.store[0] == [0,4,3]
assert h.extract_min() == [0,4,3]
assert len(h.store) == 3
assert h.extract_min() == [1,5,2]
assert len(h.store) == 2
assert h.extract_min() == [2,1,1]
assert len(h.store) == 1
