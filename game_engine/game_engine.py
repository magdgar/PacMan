import sys
import pygame
from pygame.locals import *
from objects.Container import *


class GameEngine:
    def __init__(self, window_surface):
        self.window_surface = window_surface
        with open("background/lvl2.txt") as f:
            lines = f.readlines()
        self.bg_matrix = lines

    def simulate_world(self, events):
        self.move_hero(get_object(0), events)   # pac_man

    def move_hero(self, hero, events):
        for event in events:
            if event.type == KEYDOWN:
               hero.new_direction = event.key
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        if self.in_place_to_change_direction(hero):
            hero.direction = hero.new_direction
        hero.move(hero.movements[hero.direction])

        if self.is_this_the_wall(hero):
            hero.move((hero.movements[hero.direction][0] * -1, hero.movements[hero.direction][1] * -1))

    def in_place_to_change_direction(self, hero):
        return ((hero.new_direction == K_UP or hero.new_direction == K_DOWN) and hero.x % 20 == 0) \
               or ((hero.new_direction == K_RIGHT or hero.new_direction == K_LEFT) and hero.y % 20 == 0)

    def is_this_the_wall(self, hero):
        x = round(hero.x/20)
        y = round(hero.y/20)
        return 0 < ord(self.bg_matrix[y][x:x + 1]) - 48 < 7

    def eat_dot(self, hero):
        x = round(hero.x/20)
        y = round(hero.y/20)
        self.bg_matrix[y][x:x + 1] = 0