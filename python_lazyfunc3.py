# -*- coding: utf-8 -*-

# Write  a lazy function to calculate the square for given number
def lazy_square(x):
    def square():
        return x*x
    return square

f = lazy_square(3)
print(f())
