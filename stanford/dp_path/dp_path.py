class MaxPath(object):
    def __init__(self):
        self.vertices = []

    def read_file(self, filename):
        file = open(filename, 'r')
        count = 0
        for line in file:
            if count != 0:
                self.vertices.append(int(line))
            count += 1

    
