#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

def recursive(i, j):
    if j == 0:
        return
    else:
        print(i[j - 1], end='')
        recursive(buf, j - 1)


buf = input("intpu:")
recursive(buf, len(buf))