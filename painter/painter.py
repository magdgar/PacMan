import pygame
from background.background import paint_whole_background, repaint_fragment_of_background
from events.eventobserver import EventObserver
from background.dynamic_images import DynamicImages
from pygame.rect import Rect
from media.dirtyrect import *
import background
from objects.Container import *
from objects.hero import RECT_MATRIX

BGCOLOR = (0, 0, 0)


class Painter(EventObserver):
    def __init__(self, window_surface):
        super().__init__()
        self.react_cases = {"GAME_OVER": self.paint_game_over, "REPAINT": self.repaint_background_with_dots}
        self.window_surface = window_surface
        self.window_surface.fill(BGCOLOR)
        self.save_screenshot(window_surface)
        self.dynamic_images = DynamicImages(window_surface)
        #paint_whole_background(window_surface)

        pygame.display.update()

    def paint_objects(self):
        for pac_dirty_rect in DIRTY_RECT:
            repaint_fragment_of_background(self.window_surface, pac_dirty_rect.dirty_rect, pac_dirty_rect.dot)
        for hero in get_objects():
            hero.animations[hero.direction].blit(self.window_surface, (hero.x, hero.y))
        for pac_dirty_rect in DIRTY_RECT:
            pygame.display.update(pac_dirty_rect.dirty_rect)
        clear_dirty_rect()

    def repaint_background(self, with_dots=True):
        paint_whole_background(self.window_surface)
        pygame.display.update()

    def repaint_background_with_dots(self):
        paint_whole_background(self.window_surface, True, RECT_MATRIX.map_array)
        self.dynamic_images.erase_live()
        pygame.display.update()

    def paint_game_over(self):
        pygame.Surface.blit(self.window_surface, pygame.image.load('resources/game_over.png'), (220, 260))
        self.dynamic_images.erase_live()
        for object in get_objects():
            for key, animation in object.animations.items():
                animation.stop()
        pygame.display.update()

    def save_screenshot(self, window_surface):
        paint_whole_background(window_surface, False)
        pygame.display.update()
        pygame.image.save(window_surface, "resources/levels/map.jpeg")

        paint_whole_background(window_surface, True)
        pygame.display.update()
        pygame.image.save(window_surface, "resources/levels/map_dot.jpeg")

