# -*- coding: utf-8 -*-

import functools

# def log(text = ''):
#     def decorate(func):
#         @functools.wraps(func)
#         def execute(*args, **kw):
#             print('===Before===')
#             print('Execute %s(%s): %d'%(func.__name__, text, func(*args, **kw)))
#             print('===After===')
#         return execute
#     return decorate

# def log(func):
#     @functools.wraps(func)
#     def execute(*args, **kw):
#         print('===Before===')
#         print('Execute %s: %d'%(func.__name__, func(*args, **kw)))
#         print('===After===')
#     return execute

def log(param):
    @functools.wraps(param)
    def execute(*args, **kw):
        print('===Before===')
        print('Execute %s: %d'%(param.__name__, param(*args, **kw)))
        print('===After===')

    def executeWithText(func):
        def run(*args, **kw):
            print('===Before===')
            print('Execute %s(%s): %d'%(func.__name__, param, func(*args, **kw)))
            print('===After===')
        return run

    if isinstance(param, str):
        return executeWithText
    else:
        return execute

@log
def cal_sum(*nums):
    ans = 0
    for n in nums:
        ans += n
    return ans

@log('Product')
def cal_product(*nums):
    ans = 1
    for n in nums:
        ans *= n
    return ans

cal_sum(1, 2, 3)
cal_product(4, 5, 6)
