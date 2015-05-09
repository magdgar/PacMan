__author__ = 'Makda'
import pygame
from media.dirtyrect import *


class Painter:
    def __init__(self, window_surface):
        self.window_surface = window_surface
        self.window_surface.fill((0, 0, 0))

    def paint_objects(self):
        pygame.display.update(DIRTY_RECT)
        clear_dirty_rect()