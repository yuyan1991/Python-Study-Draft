# -*- coding: utf-8 -*-

# Constructing the sequence that each element in the sequence can be divided by the given n, with filter

size = 100
# generate the sequence [1,2,3,...,n]
def generate():
    cur = 1
    while (True):
        yield cur
        if cur > size:
            break
        cur += 1
g = generate()
# for i in range(10):
#     print(next(g))

r = 3
def f(x):
    return x % r == 0
print(list(filter(f, g)))
print(list(filter(f, [x for x in range(1, size + 1)])))
