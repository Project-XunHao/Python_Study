#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 求100之内的素数。

for num in range (2,101):
    leap = 1
    for i in range(2, num):
        if num % i == 0:
            leap = 0
            break
    if leap == 1:
        print(num)
