#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import pygame
import random
from bullet import Bullet
from alien import Alien

def add_bullet(setting, screen, ship, bullets):
    # 创建一颗子弹，并加入到编组bullers中
    if ship.bullet == True:
        if setting.bullet_time == 0:
            setting.bullet_time = setting.bullet_time_interval
            new_bullet = Bullet(setting, screen, ship)
            bullets.add(new_bullet)
        else:
            setting.bullet_time -= 1

def del_bullet(setting, screen, ship, bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def add_alien(setting, screen, aliens):
    # 创建外星人舰队(多个外星人)
    # alien = Alien(setting, screen)
    if setting.alien_totle_num != setting.alien_cur_num:
        if setting.alien_time == 0:
            setting.alien_time = setting.alien_time_interval
            num = random.randint(0, setting.alien_totle_num - setting.alien_cur_num)
            for alien_num in range(0, int(num / 2.0)):
                alien = Alien(setting, screen)
                setting.alien_cur_num += 1
                aliens.add(alien)
        else:
            setting.alien_time -= 1

def del_alien(setting, screen, aliens):
    for alien in aliens.copy():
        if alien.rect.top >= alien.screen_rect.bottom \
                or alien.rect.right < 0 or alien.rect.left > alien.screen_rect.width:
            setting.alien_cur_num -= 1
            aliens.remove(alien)

def check_bullet_alien(setting, bullets, aliens):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    for key, value in collisions.items():
        setting.alien_cur_num -= 1

def update_screen(setting, screen, ship, bullets, alien):
    # 更新屏幕上的图像，并且换到新屏幕
    # 每次循环重新绘屏
    screen.fill(setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()