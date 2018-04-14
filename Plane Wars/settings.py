#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Settings():
    # 初始化游戏的设置
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # 游戏级别
        self.level = 0 + 9
        self.level_max = 10


    def update_setting(self):
        # 飞船的设置
        self.ship_speed_factor = 0.5 + self.level * 0.2

        # 子弹设置
        self.bullet_speed_factor = self.ship_speed_factor * 1.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_time_interval = (10 + (self.level_max - self.level) ** 3)
        self.bullet_time = self.bullet_time_interval

        # 同时存在的敌机数量
        self.alien_totle_num = self.level * 3 + self.level
        self.alien_cur_num = 0
        self.alien_time_interval = (self.level_max - self.level) ** 2 + 50
        self.alien_time = 0
        self.alien_speed_factor = 0.2 + self.level * 0.05


    def update_level(self):
        if self.level < self.level_max:
            self.level += 1
        self.update_setting()