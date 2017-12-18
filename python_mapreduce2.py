# -*- coding: utf-8 -*-

# Convert string into an integer via map reduce
from functools import reduce

def convert(s):
    # dict_list = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    dict_list = {}
    for i in range(10):
        dict_list[str(i)] = i
    def cal(x,y):
        return x * 10 + y
    def f(c):
        return dict_list[c]
    return reduce(cal, map(f, s))
print(convert('5201314'))
