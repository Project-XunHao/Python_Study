#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import pygame
import time
from settings import Settings
from ship import Ship
import game_func as gf
import key
from pygame.sprite import Group
from alien import Alien

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    setting = Settings()
    setting.update_level()

    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("Plane Wars")

    # 创建一艘船
    ship = Ship(setting, screen)

    # 创建子弹
    bullets = Group()

    # 创建敌机(外星人)
    aliens = Group()

    i = 0

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        key.check_events(ship, setting)
        ship.update()
        bullets.update()
        aliens.update()

        gf.del_bullet(setting, screen, ship, bullets)
        gf.add_bullet(setting, screen, ship, bullets)

        gf.add_alien(setting, screen, aliens)
        gf.del_alien(setting, screen, aliens)

        gf.check_bullet_alien(setting, bullets, aliens)

        # 刷新显示
        gf.update_screen(setting, screen, ship, bullets, aliens)



run_game()