#!/usr/bin/python
# -*- coding: UTF-8 -*-

#判断101-200之间有多少个素数，并输出所有素数。


from math import sqrt
from sys import stdout

for i in range(101,201):
    x = int(sqrt(i))
    for j in range(2, x + 1):
        if i % j == 0:
            leap = 1
            break
        else:
            leap = 0
    if leap == 0:
        print(i)
