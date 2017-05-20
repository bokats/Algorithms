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

        self.data = sorted(self.data, key=lambda x: (x[2], x[0]), reverse=True)
        print(self.data)


m = MinimizeCompletionTime()
m.read_file('data.txt')
m.minimize_by_difference()
