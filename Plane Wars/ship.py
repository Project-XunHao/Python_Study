#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygame

class Ship():
    def __init__(self, setting, screen):
        # 初始化飞船并设置初始值
        self.screen = screen
        self.setting = setting

        # 加载飞船图片并获取其外接矩形
        self.image = pygame.image.load('image/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # 移动标志
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.bullet = False

    def update(self):
        # 根据移动标志调整飞船位置
        if self.moving_left and self.rect.centerx > 0 + self.rect.width / 2:
            self.centerx -= self.setting.ship_speed_factor
        if self.moving_right and self.rect.centerx < self.screen_rect.right - self.rect.width / 2:
            self.centerx += self.setting.ship_speed_factor
        if self.moving_up and self.rect.bottom > 0 + self.rect.height:
            self.bottom -= self.setting.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.setting.ship_speed_factor

        # 根据 self.center 更新 rect 对象
        self.rect.centerx = self.centerx
        self.rect.bottom = self.bottom

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)