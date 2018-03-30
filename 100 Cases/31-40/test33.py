#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 按逗号分隔列表。

L = [1,2,3,4,5]

s1 =  ','.join(str(i) for i in L[::1])
print(s1)