def read_file(filename):
    array = []
    file = open(filename, 'r')
    for line in file:
        array.append(int(line))
    return array

print(read_file('algo1-programming_prob-2sum.txt')[0])

# def two_sum(array)
