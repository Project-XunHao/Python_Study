#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygame.font

class Scoring():
    def __init__(self, setting, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.setting = setting

        self.text_color = (255,0,0)
        self.font = pygame.font.SysFont(None, 48)

        self.score = 0

        self.prep_score()

    def prep_score(self):
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.setting.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)