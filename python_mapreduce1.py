# -*- coding: utf-8 -*-

# Given [x1, x2, ..., xn], calculate x1*x1*x1 + x2*x2*x2 + ... + xn * xn * xn via map reduce

from functools import reduce

def cal(L):
    def f(x):
        return x*x*x
    def add(x, y):
        return x + y
    return reduce(add, map(f, L))

L=[1, 2, 3]
print(cal(L))

L=[1, 2, 3, 0]
print(cal(L))

L=[1, 2, 4, 3, 0]
print(cal(L))
