import pygame
from pygame.rect import Rect
from background.background import repaint_fragment_of_background
from events.eventobserver import EventObserver
from media.constans import NUMBERS_DICT


class DynamicImages:

    def __init__(self, window_surface, cointainer):
        self.window_surface = window_surface
        self.cointainer = cointainer
        self.lives = 3

        self.live = 'resources/live.png'
        self.window_surface = window_surface
        self.last_score = 10157
        pygame.Surface.blit(self.window_surface, pygame.image.load(self.live), (100, 580))
        pygame.Surface.blit(self.window_surface, pygame.image.load(self.live), (70, 580))
        pygame.Surface.blit(self.window_surface, pygame.image.load(self.live), (40, 580))
        #pygame.Surface.blit(self.window_surface, pygame.image.load(self.live), (530, 580))
        #pygame.Surface.blit(self.window_surface, pygame.image.load(self.live), (500, 580))
        #pygame.Surface.blit(self.window_surface, pygame.image.load(self.live), (470, 580))
        #pygame.Surface.blit(self.window_surface, pygame.image.load(NUMBERS_DICT[0]), (100, 620))
        #self.repaint_score()

    def erase_live(self):
        self.lives -= 1
        repaint_fragment_of_background(self.window_surface, Rect(40 + self.lives*30, 580, 30, 30), False)

    def paint_numbers(self):
        for i in range(0, 10):
            pygame.Surface.blit(self.window_surface, pygame.image.load(NUMBERS_DICT[self.last_score]), (260 + i*30, 620))

    def repaint_score(self, score, enemy=False):
        mod = 10
        i = 0
        while score > 0:
            if enemy:
                pygame.Surface.blit(self.window_surface, pygame.image.load(NUMBERS_DICT[score % mod]), (300 - i*20, 620))
            pygame.Surface.blit(self.window_surface, pygame.image.load(NUMBERS_DICT[score % mod]), (100 - i*20, 620))
            score -= score % mod
            score /= mod
            i += 1


