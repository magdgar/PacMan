import pygame
from events.eventobserver import EventObserver

from media.dirtyrect import *
import background
from objects.container import *

BGCOLOR = (0, 0, 0)


class Painter(EventObserver):
    def __init__(self, window_surface):
        super().__init__()
        self.react_cases = {"GAME_OVER": self.paint_game_over}
        self.window_surface = window_surface
        self.window_surface.fill(BGCOLOR)

    def paint_objects(self):
        for pac_dirty_rect in DIRTY_RECT:
            background.background.repaint_fragment_of_background(self.window_surface, pac_dirty_rect.dirty_rect, pac_dirty_rect.dot)
        for hero in get_objects():
            hero.animations[hero.direction].blit(self.window_surface, (hero.x, hero.y))
        for pac_dirty_rect in DIRTY_RECT:
            pygame.display.update(pac_dirty_rect.dirty_rect)
        clear_dirty_rect()

    def paint_game_over(self):
        pygame.Surface.blit(self.window_surface, pygame.image.load('C:/Users/Maciek/PacMan/resources/inky_down_1.png'), (100, 100))
        pygame.display.update()