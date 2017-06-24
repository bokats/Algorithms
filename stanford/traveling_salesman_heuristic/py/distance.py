from math import sqrt

def calculate_distance(coord1, coord2):
    print(sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2))

calculate_distance([9983.3333,98550.0000], [10000.0000,98566.6667])
calculate_distance([10050.0000,98550.0000], [10066.6667, 98533.3333])
