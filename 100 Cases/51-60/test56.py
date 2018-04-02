#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 画图，学用circle画圆形。　　

import tkinter

canvas = tkinter.Canvas(width=800, height=600, bg='yellow')
canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
k = 1
j = 1
for i in range(0, 30):
    canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
    k += j
    j += 0.3

canvas.mainloop()