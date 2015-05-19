from pygame.constants import *
from pygame.rect import Rect
from game_engine.gameengine import *
from media.matrix import RectMatrix

RECT_MATRIX = RectMatrix(BG_MATRIX)
class Hero:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.area_rect = Rect(x + 3, y + 3, 20, 20)
        self.direction = K_DOWN
        self.new_direction = K_DOWN
        self.movements = {K_UP: (0, -self.speed), K_RIGHT: (self.speed, 0),
                          K_DOWN: (0, self.speed), K_LEFT: (-self.speed, 0),
                          K_PAUSE: (0, 0), K_BREAK: (0, 0)}
        add_object(self)

    def move_hero(self, arguments): #od logiki TODO
        pass

    def move(self):
        self.x += self.movements[self.direction][0]
        self.y += self.movements[self.direction][1]
        self.area_rect.move_ip(self.movements[self.direction][0], self.movements[self.direction][1])

    def go_back(self):
        self.x -= self.movements[self.direction][0]
        self.y -= self.movements[self.direction][1]
        self.area_rect.move_ip(-self.movements[self.direction][0], -self.movements[self.direction][1])

    def in_place_to_change_direction(self):
        return RECT_MATRIX.is_at_direction_change_place(self.area_rect)

    def is_this_the_wall(self, direction):
        return RECT_MATRIX.is_this_the_wall(self.area_rect, (int(self.movements[direction][0]/self.speed),
                                                             int(self.movements[direction][1]/self.speed)))
