class MinHeap(object):
    def __init__(self):
        self.store = []

    def get_store(self):
        return self.store

    def insert(self, node):
        self.store.append(node)
        self.heapify_up()

    def extract_min(self):
        self.store[0], self.store[-1] = self.store[-1], self.store[0]
        min_node = self.store.pop()
        self.heapify_down()
        return min_node

    def heapify_up(self):
        new_node_idx = len(self.store) - 1
        parent_idx = int((new_node_idx - 1) / 2)
        while new_node_idx != 0 and \
            self.store[new_node_idx].get_value() < self.store[parent_idx].get_value():
            self.store[new_node_idx], self.store[parent_idx] = \
            self.store[parent_idx], self.store[new_node_idx]
            new_node_idx = parent_idx
            parent_idx = int((new_node_idx - 1) / 2)

    def heapify_down(self):
        current_node_idx = 0
        swap = True
        while swap:
            swap = False
            children = self.children_indeces(current_node_idx)
            swap_idx = current_node_idx
            for child_idx in children:
                if self.store[child_idx].get_value() < self.store[swap_idx].get_value():
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
    def __init__(self, value, edge):
        self.value = value
        self.edge = edge

    def get_value(self):
        return self.value

    def get_edge(self):
        return self.edge

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
