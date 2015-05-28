import pygame
from background.background import paint_whole_background, repaint_fragment_of_background
from events.eventobserver import EventObserver

from media.dirtyrect import *
import background
from objects.Container import *

BGCOLOR = (0, 0, 0)


class Painter(EventObserver):
    def __init__(self, window_surface):
        super().__init__()
        self.react_cases = {"GAME_OVER": self.paint_game_over, "RESPAWN" : self.repaint_background}
        self.window_surface = window_surface
        self.window_surface.fill(BGCOLOR)
        paint_whole_background(window_surface)
        pygame.display.update()

    def paint_objects(self):
        for pac_dirty_rect in DIRTY_RECT:
            repaint_fragment_of_background(self.window_surface, pac_dirty_rect.dirty_rect, pac_dirty_rect.dot)
        for hero in get_objects():
            hero.animations[hero.direction].blit(self.window_surface, (hero.x, hero.y))
        for pac_dirty_rect in DIRTY_RECT:
            pygame.display.update(pac_dirty_rect.dirty_rect)
        clear_dirty_rect()

    def repaint_background(self):
        paint_whole_background(self.window_surface)
        pygame.display.update()

    def paint_game_over(self):
        for object in get_objects():
            for key, animation in object.animations.items():
                animation.stop()
        pygame.display.update()
