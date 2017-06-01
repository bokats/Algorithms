import numpy as np

class Knapsack(object):
    def __init__(self):
        self.items = None
        self.weight = 0

    def read_file(self,filename):
        file = open(filename, 'r')
        first_line = True
        count = 0
        for line in file:
            line = line.split()
            if first_line:
                self.weight = int(line[0])
                self.items = np.zeros((int(line[1]), 2), int)
                first_line = False
            else:
                self.items[count][0] = int(line[0])
                self.items[count][1] = int(line[1])
                count += 1

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

    def find_optimal_fast(self):
        prev_row = np.zeros(self.weight + 1, int)

        item_idx = 0
        while item_idx < len(self.items):
            print(item_idx)
            item = self.items[item_idx]
            new_row = np.zeros(self.weight + 1, int)
            for weight in range(len(new_row)):
                if weight < item[1]:
                    new_row[weight] = prev_row[weight]
                else:
                    new_row[weight] = max(item[0] + prev_row[weight - item[1]], prev_row[weight])
            prev_row = new_row
            item_idx += 1

        return new_row[-1]

k = Knapsack()
k.read_file('knapsack_big.txt')
# print(k.find_optimal())
print(k.find_optimal_fast())
