# -*- coding: utf-8 -*-

# 求1000,0000以内的所有质数，一开始假设全部都是素数，从小到大一个个枚举数n，然后筛掉所有n的倍数的数，缺点是每个数会被重复筛去，复杂度O(N log log N)
#  1000,0000以内的素数个数是664579，耗时23.644s

maxn = 10000000

checked = [False] * maxn
P = []

for i in range(2, maxn):
	if not checked[i]:
		P.append(i)
	for j in range(i*2, maxn, i):
		checked[j] = True

print(len(P))