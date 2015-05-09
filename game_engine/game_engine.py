__author__ = 'Makda'

import sys
import pygame
from pygame.locals import *


class GameEngine:
    def __init__(self, window_surface, hero):
        self.window_surface = window_surface
        self.hero = hero
        self.direction = K_RIGHT
        self.new_direction = K_RIGHT
        self.movements = {K_UP: (0, -self.hero.speed), K_RIGHT: (self.hero.speed, 0),
                          K_DOWN: (0, self.hero.speed), K_LEFT: (-self.hero.speed, 0), K_PAUSE: (0, 0)}

        with open("background/lvl2.txt") as f:
            lines = f.readlines()
        self.bg_matrix = lines

    def simulate_world(self, events):
        self.move_hero(events)

    def move_hero(self, events):
        for event in events:
            if event.type == KEYDOWN:
                self.new_direction = event.key
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        if self.in_place_to_change_direction():
            self.direction = self.new_direction
        self.hero.move(self.movements[self.direction])

        if self.is_this_the_wall():
            self.hero.move((self.movements[self.direction][0] * -1, self.movements[self.direction][1] * -1))
        self.hero.paint(self.window_surface, self.direction)

    def in_place_to_change_direction(self):
        return ((self.new_direction == K_UP or self.new_direction == K_DOWN) and self.hero.x % 20 == 0) \
               or ((self.new_direction == K_RIGHT or self.new_direction == K_LEFT) and self.hero.y % 20 == 0)

    def is_this_the_wall(self):
        x = round(self.hero.x/20)
        y = round(self.hero.y/20)
        return 0 < ord(self.bg_matrix[y][x:x + 1]) - 48 < 7

    def eat_dot(self):
        x = round(self.hero.x/20)
        y = round(self.hero.y/20)
        self.bg_matrix[y][x:x + 1] = 0