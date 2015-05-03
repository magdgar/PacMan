import sys

import pygame
from pygame.locals import *


class GameLoop:
    def __init__(self, window_surface, pac_man):
        self.window_surface = window_surface
        self.pac_man = pac_man
        self.direction = K_RIGHT
        self.new_direction = K_RIGHT
        self.movements = {K_UP: (0, -self.pac_man.speed), K_RIGHT: (self.pac_man.speed, 0),
                          K_DOWN: (0, self.pac_man.speed), K_LEFT: (-self.pac_man.speed, 0), K_PAUSE: (0, 0)}
        with open("background/lvl2.txt") as f:
            lines = f.readlines()
        self.bg_matrix = lines

    def move_pac_man(self, events):
        for event in events:
            if event.type == KEYDOWN:
                self.new_direction = event.key
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        if self.in_place_to_change_direction():
            self.direction = self.new_direction
        self.pac_man.move(self.movements[self.direction])
        if self.is_this_the_wall():
            self.pac_man.move((self.movements[self.direction][0] * -1, self.movements[self.direction][1] * -1))
        self.pac_man.paint(self.window_surface, self.direction)

    def in_place_to_change_direction(self):
        return ((self.new_direction == K_UP or self.new_direction == K_DOWN) and self.pac_man.x % 20 == 0) \
               or ((self.new_direction == K_RIGHT or self.new_direction == K_LEFT) and self.pac_man.y % 20 == 0)

    def is_this_the_wall(self):
        x = round(self.pac_man.x/20)
        y = round(self.pac_man.y/20)
        return 0 < ord(self.bg_matrix[y][x:x + 1]) - 48 < 7
