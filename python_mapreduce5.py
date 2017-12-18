# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    digits = {}
    for i in range(10):
        digits[str(i)] = i
    def power(base, n=2):
        res = 1
        for i in range(n):
            res *= base
        return res

    def convert(c):
        return digits[c]
    def add(x, y):
        return x * 10 + y
    st = s.split('.')
    ans = 0
    cur = 0
    for ss in st:
        x = reduce(add, map(convert, ss))
        cur += 1
        if cur > 1:
            x /= power(10, len(ss))
        ans += x
    return ans

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('Success!')
else:
    print('Failed!')
