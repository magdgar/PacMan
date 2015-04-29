from pygame.rect import *

import media.sprites
from media.dirtyrect import *
import background


class PacMan:
    def __init__(self, x, y):
        self.x = x              # x position in the matrix
        self.y = y              # y position in the matrix
        self.speed = 4
        self.animations = media.sprites.PacManAnim
        for key, animation in self.animations.items():
            animation.play()

    def paint(self, window_surface, direction):
        background.background.paint_background(window_surface, DIRTY_RECT[0])
        self.animations[direction].blit(window_surface, (self.x, self.y))  # each background png is 20x20

    def move(self, d_move):
        add_dirty_rect(Rect(self.x - self.speed, self.y - self.speed, 50, 50))
        self.x += d_move[0]
        self.y += d_move[1]
