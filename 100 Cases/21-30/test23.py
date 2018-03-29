#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

n = 50

for i in range(1, n + 1):
    j = i
    while n - j > 0:
        j += 1
        print(" ", end='')
    k = i * 2 - 1
    while k > 0:
        k -= 1
        print('*', end='')
    print('')

for i in range(1, n):
    j = i
    while j > 0:
        j -= 1
        print(" ", end='')
    k = (n - i) * 2 - 1
    while k > 0:
        k -= 1
        print('*', end='')
    print('')