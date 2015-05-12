import pygame

from media.dirtyrect import *
import background
from objects.Container import *

BGCOLOR = (0, 0, 0)


class Painter:
    def __init__(self, window_surface):
        self.window_surface = window_surface
        self.window_surface.fill(BGCOLOR)

    def paint_objects(self):
        for hero in get_objects():
            background.background.repaint_fragment_of_background(self.window_surface, DIRTY_RECT[0])
            hero.animations[hero.direction].blit(self.window_surface, (hero.x, hero.y))

        pygame.display.update(DIRTY_RECT)
        clear_dirty_rect()