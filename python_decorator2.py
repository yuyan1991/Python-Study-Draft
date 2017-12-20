# -*- coding: utf-8 -*-

import functools

def log(func):
    @functools.wraps(func)
    def delegator(*args, **kw):
        print('---Before---')
        res = func(*args, **kw)
        print('Execute %s: %d' % (func.__name__, res))
        print('---After---')
    return delegator

@log
def cal_sum(*nums):
    ans = 0
    for n in nums:
        ans += n
    return ans

@log
def cal_product(*nums):
    ans = 1
    for n in nums:
        ans *= n
    return ans

cal_sum(1, 2, 3)
cal_product(4, 5, 6)
