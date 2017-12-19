# -*- coding: utf-8 -*-

def createCounter():
    def generate():
        n=1
        while True:
            yield n
            n = n + 1
    g = generate()
    def counter():
        return next(g)
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('Success!')
else:
    print('Failed!')
