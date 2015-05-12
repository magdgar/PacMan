from game_engine.game_engine import *
from media.dirtyrect import *


class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.direction = K_RIGHT
        self.new_direction = K_RIGHT
        self.movements = {K_UP: (0, -self.speed), K_RIGHT: (self.speed, 0),
                          K_DOWN: (0, self.speed), K_LEFT: (-self.speed, 0), K_PAUSE: (0, 0)}

    def move(self):
        add_dirty_rect(Rect(self.x - self.speed, self.y - self.speed, 30, 30))