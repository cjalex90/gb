from functools import reduce

print(reduce(lambda x, y: x * y, [i for i in range(100, 1_001)]))
