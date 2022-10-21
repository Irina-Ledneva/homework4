from functools import reduce

my_list = list(range(100, 1001, 2))
print(reduce(lambda a, b: a * b, my_list))
