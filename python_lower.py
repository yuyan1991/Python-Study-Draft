# -*- coding: utf-8 -*-

def convert(L):
    return [s.lower() for s in L if isinstance(s, str) == True]

if convert([])!=[]:
    print("Case 1: Failed!")
elif convert(['Hello', 'World'])!=['hello', 'world']:
    print("Case 2: Failed!")
elif convert(['Hello', 20, 'World'])!=['hello', 'world']:
    print("Case 3: Failed!")
elif convert(['Hello', 20, 'World', None])!=['hello', 'world']:
    print("Case 4: Failed!")
elif convert(['Hello', 20, 'World', None, True])!=['hello', 'world']:
    print("Case 5: Failed!")
else:
    print("Success")
