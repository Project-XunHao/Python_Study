#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

for i in range(100,1000):
    ge = int(i % 10)
    shi = int((i / 10) % 10)
    bai = int(i / 100)
    if i == ge ** 3 + shi ** 3 + bai ** 3:
        print(i)