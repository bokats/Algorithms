import numpy as np

class Knapsack(object):
    def __init__(self):
        self.items = None
        self.max_weight = 0
        self.values = {}
        self.grid = None

    def read_file(self,filename):
        file = open(filename, 'r')
        first_line = True
        count = 0
        for line in file:
            line = line.split()
            if first_line:
                self.max_weight = int(line[0])
                self.items = np.zeros((int(line[1]), 2), int)
                first_line = False
            else:
                self.items[count][0] = int(line[0])
                self.items[count][1] = int(line[1])
                count += 1

    def find_optimal(self):
        self.grid = np.zeros((len(self.items) + 1, self.max_weight + 1), int)

        for item_idx in range(1, len(self.grid)):
            item = self.items[item_idx - 1]
            for weight in range(len(self.grid[item_idx])):
                if weight < item[1]:
                    self.grid[item_idx][weight] = self.grid[item_idx - 1][weight]
                else:
                    self.grid[item_idx][weight] = max(item[0] + self.grid[item_idx - 1][weight - item[1]], self.grid[item_idx - 1][weight])

        return self.grid[len(self.grid) - 1][len(self.grid[0]) - 1]

    def find_optimal_fast(self):
        for weight in range(self.max_weight + 1):
            self.values[weight] = [0,0]

        for item_idx in range(len(self.items)):
            item = self.items[item_idx]
            if not self.max_weight < item[1]:
                if self.values[self.max_weight - item[1]][1] < item_idx:
                    import pdb; pdb.set_trace()
                    self.find_table_values(self.max_weight - item[1], item_idx)
                self.values[self.max_weight][0] = max(item[0] + self.values[self.max_weight - item[1]][0], self.values[self.max_weight][0])
        return self.values[self.max_weight][0]

    def find_chosen_items(self):

        item_idx = len(self.items)
        weight = self.max_weight
        taken_items = []
        while item_idx > 0:
            if self.grid[item_idx][weight] > self.grid[item_idx - 1][weight]:
                taken_items.append(self.items[item_idx - 1])
                weight -= self.items[item_idx - 1][1]
            item_idx -= 1

        return taken_items

    def find_table_values(self, weight, item_idx):

        while self.values[weight][1] < item_idx:
            item = self.items[self.values[weight][1]]
            if not weight < item[1]:
                if self.values[weight - item[1]][1] < self.values[weight][1]:
                    self.find_table_values(weight - item[1], self.values[weight][1])
                self.values[weight][0] = max(item[0] + self.values[weight - item[1]][0], self.values[weight][0])
            self.values[weight][1] += 1


k = Knapsack()
# k.read_file('knapsack_big.txt')
# k.read_file('knapsack1.txt')
# k.read_file('test2.txt')
k.read_file('test3.txt')
# print(k.find_optimal())
# print(k.find_chosen_items())
print(k.find_optimal_fast())
