class TwoSum(object):
    def __init__(self, array = None):
        if array:
            self.array = array
        else:
            self.array = []
        self.set_nums = set([])

    def read_file(self, filename):
        file = open(filename, 'r')
        for line in file:
            self.array.append(int(line))
        self.set_nums = set(self.array)

    def find_two_sum(self):
        result = 0

        for t in range(-5, 2):
            print(t)
            if self.has_two_sum(t):
                result += 1
        return result

    def has_two_sum(self, t):
        seen_nums = set([])
        for num in self.set_nums:
            if t - num in seen_nums:
                self.set_nums.remove(num)
                self.set_nums.remove(t - num)
                return True
            else:
                seen_nums.add(num)
        return False

t = TwoSum()
t.read_file('algo1-programming_prob-2sum.txt')
# print(t.find_two_sum())

def has_two_sum(n, num_set):
    print(n)
    return any(((n-x) in num_set) and 2*x != n for x in num_set)
num_set = t.set_nums
two_sum = sum(has_two_sum(n, num_set) for n in range(-10000, 10001))
print(two_sum)
