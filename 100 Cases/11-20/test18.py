#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

a = 5
n = 8
sum = 0
num = 0

for i in range(0, n):
    num += a
    a = a * 10
    print(num)
    sum += num

print('sum:%d' % sum)