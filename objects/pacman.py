#from pygame.rect import *

from pygame.locals import *

import media.sprites
from media.dirtyrect import *
import background


class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.animations = media.sprites.PacManAnim
        for key, animation in self.animations.items():
            animation.play()

    def paint(self, window_surface, direction):
        background.background.paint_background(window_surface, DIRTY_RECT[0])
        self.animations[direction].blit(window_surface, (self.x, self.y))

    def move(self, d_move):
        add_dirty_rect(Rect(self.x - self.speed, self.y - self.speed, 40, 40))
        self.x += d_move[0]
        self.y += d_move[1]