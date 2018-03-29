#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

n = 10
m = 100
sum = 0

for i in range(10):
    sum += m
    m /= 2

print("sum:%lf" % sum)
print("m:%lf" % m)