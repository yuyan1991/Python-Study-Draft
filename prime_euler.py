# -*- coding: utf-8 -*-

# 求1000,0000以内的所有质数，Euler筛数法，每个数只会被筛一次，并且是被它的最小的质因子筛去，复杂度O(N)
#  1000,0000以内的素数个数是664579，耗时6.129s

maxn = 10000000

checked = [False] * (maxn+1)
P = []

for i in range(2, maxn):
	if not checked[i]:
		P.append(i)
	for p in P:
		if p * i > maxn:
			break
		checked[p*i] = True
		if i % p == 0:
			break

print(len(P))
