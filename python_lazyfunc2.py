# -*- coding: utf-8 -*-

def createCounter():
    cur = 0
    def counter():
        nonlocal cur
        cur = cur + 1
        return cur
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('Success!')
else:
    print('Failed!')
