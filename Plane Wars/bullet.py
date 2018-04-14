#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # 一个对飞船发射的子弹进行管理的类

    def __init__(self, setting, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示子弹位置
        self.y = float(self.rect.y)
        self.color = setting.bullet_color
        self.speed_factor = setting.bullet_speed_factor
        self.bullet_time_interval = setting.bullet_time_interval

    def update(self):
        # 向上移动子弹
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹 rect 的位置
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)