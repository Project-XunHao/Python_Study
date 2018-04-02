#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 画图，综合例子。

import tkinter

canvas = tkinter.Canvas(width=300, height=300, bg='green')
canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
x0 = 150
y0 = 100
canvas.create_oval(x0 - 10, y0 - 10, x0 + 10, y0 + 10)
canvas.create_oval(x0 - 20, y0 - 20, x0 + 20, y0 + 20)
canvas.create_oval(x0 - 50, y0 - 50, x0 + 50, y0 + 50)

import math

B = 0.809

for i in range(16):
    a = 2 * math.pi / 16 * i
    x = math.ceil(x0 + 48 * math.cos(a))
    y = math.ceil(y0 + 48 * math.sin(a) * B)
    canvas.create_line(x0, y0, x, y, fill='red')
canvas.create_oval(x0 - 60, y0 - 60, x0 + 60, y0 + 60)


for k in range(180):
        a = (2 * math.pi / 180) * k
        x = math.ceil(x0 + 48 * math.cos(a))
        y = math.ceil(y0 + 48 * math.sin(a) * B)
        canvas.create_line(x0, y0+100, x, y+100, fill='red')

        a = (2 * math.pi / 180) * k
        x = math.ceil(x0 + 48 * math.cos(a))
        y = math.ceil(y0 + 48 + math.sin(a) * B)
        canvas.create_line(x0, y0+150, x, y+150, fill='red')

canvas.mainloop()