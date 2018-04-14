#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # 表示一个外星人的类

    def __init__(self, setting, screen):
        super(Alien, self).__init__()
        self.setting = setting
        self.screen = screen

        # 加载外星人图片
        self.image = pygame.image.load('image/alien.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 每个外星人最初在屏幕上的位置
        self.rect.y = self.rect.height
        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)

        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.direct = random.randint(0, 1)
        self.direct_size = random.randint(1, 10)

    def update(self):
        if self.direct == 0:
            self.x -= self.direct_size / 100.0
        else:
            self.x += self.direct_size / 100.0
        self.y += self.setting.alien_speed_factor
        self.rect.y = self.y
        self.rect.x = self.x

    def blitme(self):
        # 在指定位置绘制外星人
        self.screen.blit(self.image, self.rect)