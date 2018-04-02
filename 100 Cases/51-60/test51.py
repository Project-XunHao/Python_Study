#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 学习使用按位与 & 。

a = 0o77 # 注意 字母 'o' 和数字 '0' 的区别
b = a & 3
print('a & b = %d' % b)
b &= 7
print('a & b = %d' % b)