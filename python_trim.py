# -*- coding: utf-8 -*-

def trim(s):
    if s[0:1]==' ':
        return trim(s[1:])
    elif s[-1:]==' ':
        return trim(s[0:-1])
    return s

if trim('hello   ')!='hello':
    print("1. Failed!")
elif trim('   hello')!='hello':
    print("2. Failed!")
elif trim('  hello  ')!='hello':
    print("3. Failed!")
elif trim('hello')!='hello':
    print("4. Failed!")
elif trim('  hello world  ')!='hello world':
    print("5. Failed!")
elif trim('')!='':
    print("6. Failed!")
elif trim('    ')!='':
    print("7. Failed!")
else:
    print("Success!")
