# -*- coding: utf-8 -*-
A = 'ABC'
B = 'XYZ'
print([x+y for x in A if x!='A' for y in B if y != 'X'])
print([x+y for x in A for y in B if x!='A' and y != 'X'])
