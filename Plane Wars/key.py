#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import pygame

def check_keydown_events(event, ship, setting):
    if event.key == pygame.K_LEFT:
        # 飞船左移
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        ship.bullet = True
        setting.bullet_time = 0

def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT:
        # 飞船左移
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_SPACE:
        ship.bullet = False

def check_events(ship, setting):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, setting)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)