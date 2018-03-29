#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

# num = int(input('input:'))
num = 255

print('%d = ' % num, end='')
while num not in [1]:
    for i in range(2, num + 1):
        if num % i == 0:
            num = int(num / i)
            if num != 0:
                if num == 1:
                    print('%d' % i)
                else:
                    print('%d * ' % i, end='')
                break