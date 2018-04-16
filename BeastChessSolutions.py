# -*- coding: utf-8 -*-

# 计算斗兽棋的合法局面数

WIDTH = 7
HEIGHT = 9
CHESS_SIZE = WIDTH * HEIGHT
RIVER_SIZE = 6 * 2
AVAILABLE_SIZE_MICE = CHESS_SIZE - 2 #默认双方的兽穴不能占
AVAILABLE_SIZE_OTHERS = CHESS_SIZE - RIVER_SIZE - 2
CHESS_PIECES = 16	# 把前两个棋子当成是双方的老鼠

f = [[[0 for i in range(CHESS_PIECES + 1)] for i in range(CHESS_PIECES + 1)] for i in range(2)]

def debugMode(n, m, l, turnOn):
	if not turnOn:
		return
	for j in range(m + 1):
		for k in range(l + 1):
			for i in range(n):
				print('f[%d][%d][%d] = %d'%(i, j, k, f[i][j][k]))

if __name__=='__main__':
	f[0][0][0] = f[1][0][0] = 1
	f[0][0][1] = AVAILABLE_SIZE_MICE
	for i in range(1, CHESS_PIECES):
		available = AVAILABLE_SIZE_OTHERS
		if i == 1:
			available = AVAILABLE_SIZE_MICE
		for j in range(i+1 + 1):
			f[0][i][j] = f[0][i-1][j]
			if j-1>=0:
				f[0][i][j] += f[0][i-1][j-1] * (available - j + 1)
			f[1][i][j] = f[1][i-1][j] + f[0][i-1][j]
			if j-1>=0:
				f[1][i][j] += f[1][i-1][j-1] * (available - j + 1)
	ans = 0
	for i in range(CHESS_PIECES + 1):
		ans += f[0][CHESS_PIECES - 1][i] + f[1][CHESS_PIECES - 1][i]

	debugMode(2, 2, 2, True)
	print(ans)
