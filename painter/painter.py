import pygame

from media.dirtyrect import *
import background
from objects.container import *

BGCOLOR = (0, 0, 0)


class Painter:
    def __init__(self, window_surface):
        self.window_surface = window_surface
        self.window_surface.fill(BGCOLOR)

    def paint_objects(self):
        for pac_dirty_rect in DIRTY_RECT:
            background.background.repaint_fragment_of_background(self.window_surface, pac_dirty_rect.dirty_rect,
                                                                 pac_dirty_rect.dot)
        for hero in get_objects():
            hero.animations[hero.direction].blit(self.window_surface, (hero.x, hero.y + 1))
        for pac_dirty_rect in DIRTY_RECT:
            pygame.display.update(pac_dirty_rect.dirty_rect)
        clear_dirty_rect()