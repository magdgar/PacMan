import pygame
from pygame.rect import Rect
from background.background import repaint_fragment_of_background
from events.eventobserver import EventObserver
from media.constans import NUMBERS_DICT
from objects.Container import get_object


class DynamicImages:

    def __init__(self, window_surface):
        self.lives = 3
        self.window_surface = window_surface
        self.live = 'resources/live.png'
        self.window_surface = window_surface
        self.last_score = 10157
        pygame.Surface.blit(self.window_surface, pygame.image.load(self.live), (100, 580))
        pygame.Surface.blit(self.window_surface, pygame.image.load(self.live), (70, 580))
        pygame.Surface.blit(self.window_surface, pygame.image.load(self.live), (40, 580))
        pygame.Surface.blit(self.window_surface, pygame.image.load(NUMBERS_DICT[0]), (540, 580))
        #self.repaint_score()

    def erase_live(self):
        self.lives -= 1
        repaint_fragment_of_background(self.window_surface, Rect(40 + self.lives*30, 580, 30, 30), False)

    def paint_numbers(self):
        for i in range(0, 10):
            pygame.Surface.blit(self.window_surface, pygame.image.load(NUMBERS_DICT[self.last_score]), (260 + i*30, 580))

    def repaint_score(self):
        mod = 10
        i = 0
        score = get_object(0).score
        print(score)
        while score >= mod:
            pygame.Surface.blit(self.window_surface, pygame.image.load(NUMBERS_DICT[score%mod]), (540 - i*20, 580))
            score -= score%mod
            score /= mod
            i += 1
        pygame.Surface.blit(self.window_surface, pygame.image.load(NUMBERS_DICT[score%mod]), (540 - i*20, 580))



