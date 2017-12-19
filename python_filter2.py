# -*- coding: utf-8 -*-

# Generate all the prime below 1000 with filter

maxn = 1000 + 1

def generate():
    cur = 2
    while True:
        yield cur
        cur += 1

# g = generate()
# for i in range(3, maxn, 2):
#      print(next(g))

def _not_divisible_(n):
    return lambda x: x % n > 0

def prime():
    g = generate()
    while True:
        n = next(g)
        yield n
        g = filter(_not_divisible_(n), g)

for p in prime():
    if p >= maxn:
        break
    print(p)
