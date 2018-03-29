#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

num = input('input:')

l = len(num)
n = int(l / 2)
leap = 0
for i in range(n):
    j = 0 - (i + 1)
    if num[i] != num[j]:
        leap = 1

if leap == 1:
    print('Error.')
else:
    print('OK.')

