#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 时间函数举例2。

import time

start = time.time()
for i in range(30000):
    print(i)
end = time.time()

print(end - start)