class MinHeap(object):
    def __init__(self):
        self.store = []

    def insert(self, node):
        self.store.append(node)
        self.heapify_up()

    def extract_min(self):
        self.store[0], self.store[-1] = self.store[-1], self.store[0]
        min_node = self.store.pop()
        self.heapify_down()

    def heapify_up(self):
        new_node_idx = len(self.store) - 1
        parent_idx = (new_node_idx - 1) / 2
        while new_idx_idx != 0 and \
            self.store[new_node_idx].get_value() < self.store[parent_idx].get_value():
            self.store[new_node_idx], self.store[parent_idx] = \
            self.store[parent_idx], self.store[new_node_idx]
            new_node_idx = parent_idx
            parent_idx = (new_node_idx - 1) / 2

    def heapify_down(self):
        current_node_idx = 0
        swap = True
        while swap:
            swap = False
            children = self.children_indeces(current_node_idx)
            swap_idx = current_node_idx
            for child_idx in children:
                if self.store[child_idx] < self.store[swap_idx]:
                    swap_idx = child_idx
                    swap = True
            if swap:
                self.store[current_node_idx], self.store[swap_idx] = \
                self.store[swap_idx], self.store[current_node_idx]
                current_node_idx = swap_idx
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

class Node(object):
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value
