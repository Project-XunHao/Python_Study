#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 求1+2!+3!+...+20!的和。

sum = 1
num = 0
n = 20

for i in range(1, n + 1):
    sum = 1
    while i > 1:
        sum *= i
        i -= 1
    num += sum

print(num)