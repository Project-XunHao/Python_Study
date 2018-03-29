#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

'''
方法一：
'''
num = input('input:')

def recursive(one_str):
    print('.%s' % one_str);
    if len(one_str) <= 1:
        return one_str
    return one_str[-1] + recursive(one_str[:-1])

print(recursive(num))


'''
方法二：
'''
'''
print(num[::-1])
'''


