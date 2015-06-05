import pygame
from pygame.rect import Rect
from background.background import repaint_fragment_of_background
from media.constans import NUMBERS_DICT
class DynamicImages:

    def __init__(self, window_surface):
        self.lives = 3
        self.window_surface = window_surface
        self.live = 'resources/live.png'
        self.window_surface = window_surface
        pygame.Surface.blit(self.window_surface, pygame.image.load(self.live), (100, 580))
        pygame.Surface.blit(self.window_surface, pygame.image.load(self.live), (70, 580))
        pygame.Surface.blit(self.window_surface, pygame.image.load(self.live), (40, 580))

        self.paint_numbers()

    def erase_live(self):
        self.lives -= 1
        repaint_fragment_of_background(self.window_surface, Rect(40 + self.lives*30, 580, 30, 30), False)

    def paint_numbers(self):
        for i in range(0, 10):
            pygame.Surface.blit(self.window_surface, pygame.image.load(NUMBERS_DICT[i]), (260 + i*30, 580))
