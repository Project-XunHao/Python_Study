#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 请抓住分子与分母的变化规律。

Molecular1 = 2 # 分子
Molecular2 = 3

Denominator1 = 1 # 分母
Denominator2 = 2

n = 20
sum = 0

for i in range(20):
    sum += Molecular1 / Denominator1
    Molecular2 = Molecular1 + Molecular2
    Molecular1 = Molecular2 - Molecular1
    Denominator2 = Denominator1 + Denominator2
    Denominator1 = Denominator2 - Denominator1

print(sum)