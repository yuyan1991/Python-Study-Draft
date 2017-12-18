# -*- coding: utf-8 -*-

def cal(x, y, f):
    return f(x) + f(y)

print(cal(-5, 6, abs))
