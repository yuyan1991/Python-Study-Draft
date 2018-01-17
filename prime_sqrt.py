# -*- coding: utf-8 -*-

# 求1000,0000以内的所有质数，直接一个个枚举n，然后枚举所有之前已经算出的质数p，满足p<=sqrt(n)，复杂度O(N*sqrt(N))，但实际速度会更快，因为用来检测的素数的个数会小于sqrt(N)
#  1000,0000以内的素数个数是664579，耗时54.759s

maxn = 10000000

P = []
for n in range(2, maxn):
    okay = True
    for p in P:
        if p * p > n:
            break
        if n % p == 0:
            okay = False
            break
    if okay:
        P.append(n)

print(len(P))
# ans=0
# for p in P:
# 	if p * p < maxn:
# 		ans+=1
# print(ans)
