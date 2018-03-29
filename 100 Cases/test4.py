#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入某年某月某日，判断这一天是这一年的第几天？

mouths = (0,31,59,90,120,151,181,212,243,273,304,334)

year = int(input("Year:"))
mouth = int(input("Mouth:"))
day = int(input("Day:"))
if 0 < mouth <= 12:
    sum = mouths[mouth - 1]
else:
    print('moutn err!')

sum += day
leap = 0
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    leap = 1
if leap == 1 and mount > 2:
    sum += 1

print("ret = %d" % sum)