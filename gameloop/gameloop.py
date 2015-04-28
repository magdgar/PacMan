import sys

import pygame
from pygame.locals import *


UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


class GameLoop:
    def __init__(self, window_surface, pac_man):
        self.window_surface = window_surface
        self.pushed_buttons = 0
        self.pac_man = pac_man
        self.direction = RIGHT

    #with open("background/lvl2.txt") as f:
         #lines = f.readlines()

    def move_pac_man(self, events):
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                self.pushed_buttons += 1
                if event.key == K_UP:
                    self.direction = UP
                elif event.key == K_RIGHT:
                    self.direction = RIGHT
                elif event.key == K_DOWN:
                    self.direction = DOWN
                elif event.key == K_LEFT:
                    self.direction = LEFT
            elif event.type == KEYUP:
                self.pushed_buttons -= 1

        if self.pushed_buttons > 0:
            if self.direction == UP:
                self.pac_man.move(0, -1)
            elif self.direction == RIGHT:
                self.pac_man.move(1, 0)
            elif self.direction == DOWN:
                self.pac_man.move(0, 1)
            elif self.direction == LEFT:
                self.pac_man.move(-1, 0)

            self.pac_man.paint(self.window_surface, self.direction)
        else:
            self.pac_man.paint(self.window_surface, self.direction)