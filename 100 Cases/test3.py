#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

i = 1
while i < 10000:
    x = i + 100
    y = i + 100 + 168
    a = int(x ** 0.5)
    b = int(y ** 0.5)
    if a * a == x and b * b == y:
        print('Value:%d' % i)
    i += 1


