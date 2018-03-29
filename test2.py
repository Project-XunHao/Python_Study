#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%；
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

i = int(input('净利润：'))

arr = [0,100000,200000,400000,600000,1000000,1000000]
rat = [0,0.1,0.075,0.05,0.03,0.015,0.01]
k = 0

for j in range(1, 7):
    if i <= arr[j]:
        k += (i - arr[j - 1]) * rat[j]
        break
    else:
        k += (arr[j] - arr[j - 1]) * rat[j]


print('奖金：%f' % k)