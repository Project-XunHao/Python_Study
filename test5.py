#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入三个整数x,y,z，请把这三个数由小到大输出。

buf = []
for i in range(3):
    num = int(input('input:'))
    buf.append(num)

buf.sort()
print(buf)