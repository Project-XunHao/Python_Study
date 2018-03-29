#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。



for j in range(1, 1001):
    num = j
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == j:
        print(sum)