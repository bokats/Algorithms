class MinimizeCompletionTime(object):
    def __init__(self):
        self.data = []

    def read_file(self, filename):
        file = open(filename, 'r')
        for line in file:
            task = line.split(" ")
            if len(task) > 1:
                self.data.append([int(task[0]), int(task[1])])

    def minimize_by_difference(self):
        for task in self.data:
            task.append(task[0] - task[1])

        current_length = 0
        weighted_avg_time = 0
        for task in sorted(self.data, key=lambda x: (x[2], x[0]), reverse=True):
            current_length += task[1]
            weighted_avg_time += task[0] * current_length

        return weighted_avg_time

    def minimize_by_ratio(self):
        for task in self.data:
            task.append(task[0] / task[1])

        current_length = 0
        weighted_avg_time = 0
        for task in sorted(self.data, key=lambda x: x[2], reverse=True):
            current_length += task[1]
            weighted_avg_time += task[0] * current_length

        return weighted_avg_time



# m = MinimizeCompletionTime()
# m.read_file('data.txt')
# print(m.minimize_by_difference())
#
# m = MinimizeCompletionTime()
# m.read_file('data.txt')
# print(m.minimize_by_ratio())
