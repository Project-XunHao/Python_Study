#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 画图，学用line画直线。

import tkinter

canvas = tkinter.Canvas(width=300, height=300, bg='green')
canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)

x0 = 263
y0 = 263
y1 = 275
x1 = 275
for i in range(19):
    canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
    x0 = x0 - 5
    y0 = y0 - 5
    x1 = x1 + 5
    y1 = y1 + 5

x0 = 263
y1 = 275
y0 = 263
for i in range(21):
    canvas.create_line(x0, y0, x0, y1, fill='red')
    x0 += 5
    y0 += 5
    y1 += 5

canvas.mainloop()