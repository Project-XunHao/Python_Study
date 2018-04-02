#!/usr/bin/python
# -*- coding: UTF-8 -*-

#　打印出杨辉三角形（要求打印出10行如下图）。

n = 20
a = []
for i in range(n):
    a.append([])
    for j in range(i + 1):
        a[i].append(0)
    for j in range(i + 1):
        if j == 0 or j == i or i < 2:
            a[i][j] = 1
        else:
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]



for i in range(n):
    for j in range(i + 1):
        print('%-6d' % a[i][j], end='')
    print('')