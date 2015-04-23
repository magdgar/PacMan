__author__ = 'Makda'

import pygame


class Dot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def paint(self, window_surface):
        pygame.draw.circle(window_surface, (255, 224, 149), (self.x, self.y), 4)