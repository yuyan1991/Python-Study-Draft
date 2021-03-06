# -*- coding: utf-8 -*-
import time, functools

def metric(func):
    @functools.wraps(func)
    def fn(*args, **kw):
        print('%s executed in %s ms' % (func.__name__, 10.24))
        return func(*args, **kw)
    return fn

# Test
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('Case 1: Failed!')
elif s != 7986:
    print('Case 2: Failed!')
