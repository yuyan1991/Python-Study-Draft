# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    delta=b*b-4*a*c
    if delta<0:
        return None, None
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    return x1, x2

params=[(1,2,1), (2,3,1), (1,3,-4), (1,1,1)]

cur=0
for para in params:
    cur = cur + 1
    x1,x2=quadratic(para[0], para[1], para[2])
    if x1 is None and x2 is None:
        print("Case %d: No solution!"%cur)
    else:
        print("Case %d: x1=%.2f, x2=%.2f"%(cur, x1, x2))
