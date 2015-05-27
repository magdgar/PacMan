from pygame.constants import *
from pygame.rect import Rect
from events.eventobserver import EventObserver
from game_engine.gameengine import BG_MATRIX, add_object
from media.matrix import RectMatrix

RECT_MATRIX = RectMatrix(BG_MATRIX) #static field to all hero object
class Hero(EventObserver):

    def __init__(self, x, y):
        super().__init__()
        self.map_point = (y, x) #cooridnates on map.txt
        self.x = x * 20 - 3 # coordinates used to paint object
        self.y = y * 20 - 3
        self.speed = 2
        self.active = True
        self.area_rect = Rect(self.x + 3, self.y + 3, 20, 20)
        self.direction = K_RIGHT
        self.new_direction = K_RIGHT
        self.movements = {K_UP: (0, -self.speed), K_RIGHT: (self.speed, 0),
                          K_DOWN: (0, self.speed), K_LEFT: (-self.speed, 0)}
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

    def get_proper_random_direction(self):
        if not self.is_this_the_wall(K_UP):
            return K_UP
        elif not self.is_this_the_wall(K_RIGHT):
            return K_RIGHT
        elif not self.is_this_the_wall(K_DOWN):
            return K_DOWN
        elif not self.is_this_the_wall(K_LEFT):
            return K_LEFT

    def in_place_to_change_direction(self):
        return RECT_MATRIX.is_at_direction_change_place(self.area_rect)

    #checks if next point with givien direction to current hero map_point have wall on it
    def is_this_the_wall(self, direction):
        return RECT_MATRIX.is_this_the_wall(self.area_rect, (int(self.movements[direction][0]/self.speed),
                                                             int(self.movements[direction][1]/self.speed)))
