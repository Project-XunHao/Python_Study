#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# Sunday Monday Tuseday Wednesday Thursday Firday Saturday

buf = input('input:')

if buf[0].upper() == 'S':
    if buf[1].lower() == 'u':
        print("星期天")
    elif buf[1].lower() == 'a':
        print("星期六")
    else:
        print("Error.")
elif buf[0].upper() == 'M':
    print("星期一")
elif buf[0].upper() == 'W':
    print("星期三")
elif buf[0].upper() == 'T':
    print("星期一")
else:
    print(buf[0].upper())