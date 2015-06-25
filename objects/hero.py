from random import randint
from pygame.constants import *
from pygame.rect import Rect
from events.eventobserver import EventObserver

PLAYER_ONE_KEYS = [K_LEFT, K_UP, K_RIGHT, K_DOWN]
PLAYER_TWO_KEYS = [K_a, K_w, K_d, K_s]


class Hero(EventObserver):

    def __init__(self, x, y, rect_martix, container, evenent_handler):
        super().__init__(container, evenent_handler)
        self.rect_matrix = rect_martix
        self.map_point = (y, x) #cooridnates on map.txt
        self.x = x * 20 - 3 # coordinates used to paint object
        self.y = y * 20 - 3
        self.speed = 2
        self.active = True
        self.area_rect = Rect(self.x + 3, self.y + 3, 20, 20)
        self.direction = K_RIGHT
        self.new_direction = K_RIGHT
        self.movements = {K_UP: (0, -self.speed), K_RIGHT: (self.speed, 0),
                          K_DOWN: (0, self.speed), K_LEFT: (-self.speed, 0),
                          K_w: (0, -self.speed), K_d: (self.speed, 0),
                          K_s: (0, self.speed), K_a: (-self.speed, 0),
                          K_DELETE: (0, 0)}

    def move_hero(self, arguments):
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
        directions = []
        if self.direction in PLAYER_ONE_KEYS:
            for direction in PLAYER_ONE_KEYS :
                if not self.is_this_the_wall(direction):
                    directions.append(direction)
            return directions[randint(0, len(directions) - 1)]
        else:
            for direction in PLAYER_TWO_KEYS:
                if not self.is_this_the_wall(direction):
                    directions.append(direction)
            return directions[randint(0, len(directions) - 1)]

    def in_place_to_change_direction(self):
        return self.rect_matrix.is_at_direction_change_place(self.area_rect)

    #checks if next point with givien direction to current hero map_point have wall on it
    def is_this_the_wall(self, direction):
         return self.rect_matrix.is_this_the_wall(self.area_rect, (int(self.movements[direction][0]/self.speed),
                                                             int(self.movements[direction][1]/self.speed)))

    def reload_movements(self):
        self.movements = {K_UP: (0, -self.speed), K_RIGHT: (self.speed, 0),
                          K_DOWN: (0, self.speed), K_LEFT: (-self.speed, 0),
                          K_DELETE: (0, 0)}

    def teleport(self, map_point):
        self.map_point = map_point #cooridnates on map.txt
        self.x = map_point[1] * 20 - 3 # coordinates used to paint object
        self.y = map_point[0] * 20 - 3
        self.area_rect = Rect(self.x + 3, self.y + 3, 20, 20)





