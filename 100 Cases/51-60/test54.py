#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 把一个整数 a 的 0~3 位置 0。

a = 9
d = a & 0xf0
print('%o\t%o' %(a,d))