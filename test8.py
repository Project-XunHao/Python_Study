#!/usr/bin/python
# -*- coding: UTF-8 -*-

#输出 9*9 乘法口诀表。

for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            print("%d*%d=%-2d " %(i,j,i*j), end="")
    print('')