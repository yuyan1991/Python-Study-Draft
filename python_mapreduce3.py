# -*- coding: utf-8 -*-

# Convert the display format for name list

def normalize(s):
    ans=''
    for i in range(len(s)):
        if i == 0:
            ans += s[i].upper()
        else:
            ans += s[i].lower()
    return ans

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
