#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

buf = input('input:')

letters = 0
space = 0
digit = 0
others = 0
i = 0

while i < len(buf):
    c = buf[i]
    i += 1
    if c.isdigit():
        digit += 1
    elif c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    else:
        others += 1

print('letters:%d' % letters)
print('space:%d' % space)
print('digit:%d' % digit)
print('others:%d' % others)