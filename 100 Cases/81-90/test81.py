#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。
# 求??代表的两位数，及809*??后的结果。

for i in range(10,100):
    a = 809 * i
    b = 800 * i
    c = 9 * i
    d = b + c
    if a > 999 and b > 999 and c > 99:
        if a == d:
            print(i)
            break