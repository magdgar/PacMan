import pygame
from background.background import paint_whole_background, repaint_fragment_of_background
from events.eventobserver import EventObserver
from background.dynamic_images import DynamicImages
from pygame.rect import Rect
from media.dirtyrect import *
import background
from objects.Container import *
from events.eventconstans import *
BGCOLOR = (0, 0, 0)


class Painter(EventObserver):
    def __init__(self, window_surface, coinainer, event_handler, rect_matrix):
        super().__init__(coinainer, event_handler)
        self.dirt_rect = []
        self.rect_matrix = rect_matrix
        self.react_cases = {GAME_OVER: self.paint_game_over, REPAINT: self.repaint_background_with_dots,
                            WON: self.paint_game_won, EAT_DOT: self.repaint_score}
        self.window_surface = window_surface
        self.window_surface.fill(BGCOLOR)
        self.save_screenshot(window_surface)
        self.dynamic_images = DynamicImages(window_surface, coinainer)
        #paint_whole_background(window_surface)

        pygame.display.update()

    def repaint_score(self):
        self.dynamic_images.repaint_score()
        pygame.display.update()

    def paint_objects(self):
        for pac_dirty_rect in self.dirt_rect:
            repaint_fragment_of_background(self.window_surface, pac_dirty_rect.dirty_rect, pac_dirty_rect.dot)
        for hero in self.container.game_objects:
            hero.current_anim[hero.direction].blit(self.window_surface, (hero.x, hero.y))
        for pac_dirty_rect in self.dirt_rect:
            pygame.display.update(pac_dirty_rect.dirty_rect)
        self.clear_dirty_rect()

    def add_dirty_rect(self, pac_dirty_rect):
        self.dirt_rect.append(pac_dirty_rect)

    def clear_dirty_rect(self):
        del self.dirt_rect[:]

    def repaint_background(self):
        paint_whole_background(self.window_surface)
        pygame.display.update()

    def repaint_background_with_dots(self):
        paint_whole_background(self.window_surface, True, self.rect_matrix.map_array)
        self.dynamic_images.erase_live()
        pygame.display.update()

    def paint_game_over(self):
        pygame.Surface.blit(self.window_surface, pygame.image.load('resources/game_over.png'), (220, 260))
        self.dynamic_images.erase_live()
        for object in self.container.ghosts:
            for key, animation in object.animations.items():
                animation.stop()
        pygame.display.update()

    def paint_game_won(self):
        pygame.Surface.blit(self.window_surface, pygame.image.load('resources/won.png'), (0, 0))
        self.dynamic_images.erase_live()
        for object in self.container.ghosts:
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

