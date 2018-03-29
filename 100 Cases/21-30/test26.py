#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 利用递归方法求5!。

def recursive(i):
    if i == 0:
        return 1
    else:
        return i * recursive(i - 1)

print(recursive(5))