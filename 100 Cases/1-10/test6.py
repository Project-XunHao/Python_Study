#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 斐波那契数列。 0、1、1、2、3、5、8、13、21、34、……。

i = 0
j = 1

buf = []
for x in range(20):
    buf.append(i)
    k = i
    i = j
    j += k

print(buf)