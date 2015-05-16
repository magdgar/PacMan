import sys

import pygame
from pygame.locals import *

from media.dirtyrect import add_dirty_rect
import media.sprites
from objects.hero import Hero
from game_engine.gameengine import BG_MATRIX
from media.dirtyrect import PacDirtyRect


class PacMan(Hero):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.animations = media.sprites.PacManAnim
        for key, animation in self.animations.items():
            animation.play()

    def move(self):
        super().move()
        add_dirty_rect(PacDirtyRect(Rect(self.x - self.speed, self.y - self.speed, 30, 35), False))

    def move_hero(self, arguments):

        hero = arguments[0]
        events = arguments[1]
        for event in events:
            if event.type == KEYDOWN:
               hero.new_direction = event.key
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        if self.in_place_to_change_direction(hero):
            hero.direction = hero.new_direction

        self.eat_dot(self)
        hero.move()

        if self.is_this_the_wall(hero):
            hero.go_back()

    @staticmethod
    def eat_dot(hero):
        x = round(hero.x/20)
        y = round(hero.y/20)
        BG_MATRIX[y][x] = 0

