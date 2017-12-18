# -*- coding: utf-8 -*-
from functools import reduce

def prod(L):
    def add(x, y):
        return x * y
    return reduce(add, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('Success!')
else:
    print('Failed!')
