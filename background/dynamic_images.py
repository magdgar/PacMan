import pygame
from pygame.rect import Rect
from background.background import repaint_fragment_of_background
from events.eventobserver import EventObserver
from media.constans import NUMBERS_DICT


class DynamicImages:
    def __init__(self, window_surface, cointainer):
        self.window_surface = window_surface
        self.cointainer = cointainer
        self.lives_left = 3
        self.enemy_lives_left = 3
        self.live = 'resources/live.png'
        self.window_surface = window_surface
        self.last_score = 10157
        self.paint_lives(100)
        if self.cointainer.enemy_pac_man is not None:
            self.paint_lives(530)
        pygame.display.update()

    def paint_lives(self, x):
        for y in range(3):
            pygame.Surface.blit(self.window_surface, pygame.image.load(self.live), (x, 580))
            x -= 30

    def erase_live(self, enemy=False):
        if not enemy:
            self.lives_left -= 1
            repaint_fragment_of_background(self.window_surface, Rect(40 + self.lives_left * 30, 580, 30, 30), False)
        else:
            self.enemy_lives_left -= 1
            repaint_fragment_of_background(self.window_surface, Rect(470 + self.enemy_lives_left * 30, 580, 30, 30), False)

    def paint_numbers(self):
        for i in range(0, 10):
            pygame.Surface.blit(self.window_surface, pygame.image.load(NUMBERS_DICT[self.last_score]), (260 + i*30, 620))

    def repaint_score(self, score, enemy=False):
        mod = 10
        i = 0
        while score > 0:
            if enemy:
                pygame.Surface.blit(self.window_surface, pygame.image.load(NUMBERS_DICT[score % mod]), (535 - i*20, 620))
            else:
                pygame.Surface.blit(self.window_surface, pygame.image.load(NUMBERS_DICT[score % mod]), (105 - i*20, 620))
            score -= score % mod
            score /= mod
            i += 1


