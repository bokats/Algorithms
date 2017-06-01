import numpy as np

class Knapsack(object):
    def __init__(self):
        self.items = []
        self.weight = 0

    def read_file(self,filename):
        file = open(filename, 'r')
        first_line = True
        for line in file:
            line = line.split()
            if first_line:
                self.weight = int(line[0])
                first_line = False
            else:
                self.items.append([int(line[0]), int(line[1])])

    def find_optimal(self):
        grid = np.zeros((len(self.items) + 1, self.weight + 1), int)

        for item_idx in range(1, len(grid)):
            item = self.items[item_idx - 1]
            for weight in range(len(grid[item_idx])):
                if weight < item[1]:
                    grid[item_idx][weight] = grid[item_idx - 1][weight]
                else:
                    grid[item_idx][weight] = max(item[0] + grid[item_idx - 1][weight - item[1]], grid[item_idx - 1][weight])

        return grid[len(grid) - 1][len(grid[0]) - 1]

k = Knapsack()
k.read_file('knapsack1.txt')
print(k.find_optimal())
