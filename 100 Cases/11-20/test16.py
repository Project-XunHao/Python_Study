#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输出指定格式的日期。
# 程序分析：使用 datetime 模块。

import datetime

if __name__ == '__main__':
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%d/%m/%Y'))

    # 创建日期对象
    Date = datetime.date(1941, 1, 5)

    print(Date.strftime('%d/%m/%Y'))

    # 日期算术运算
    NextDay = Date + datetime.timedelta(days=1)

    print(NextDay.strftime('%d/%m/%Y'))

    # 日期替换
    NextYear = Date.replace(year=Date.year + 1)

    print(NextYear.strftime('%d/%m/%Y'))