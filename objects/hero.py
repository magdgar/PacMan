from game_engine.gameengine import *


class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.direction = K_UP
        self.new_direction = K_UP
        self.movements = {K_UP: (0, -self.speed), K_RIGHT: (self.speed, 0),
                          K_DOWN: (0, self.speed), K_LEFT: (-self.speed, 0), K_PAUSE: (0, 0)}
        add_object(self)

    def move_hero(self, arguments):  # od logiki TODO
        pass

    def move(self):
        self.x += self.movements[self.direction][0]
        self.y += self.movements[self.direction][1]

    def go_back(self):
        self.x -= self.movements[self.direction][0]
        self.y -= self.movements[self.direction][1]

    @staticmethod
    def in_place_to_change_direction(hero):
        return ((hero.new_direction == K_UP or hero.new_direction == K_DOWN) and (hero.x + 2) % 20 == 0) \
               or ((hero.new_direction == K_RIGHT or hero.new_direction == K_LEFT) and (hero.y + 4) % 20 == 0) \
 \
    @staticmethod
    def is_this_the_wall(hero):
        if hero.x < 20:
            x1 = round((hero.x - 6) / 20)
        else:
            x1 = round((hero.x - 8) / 20)
        x2 = round((hero.x + 12) / 20)
        y1 = round((hero.y - 4) / 20)
        y2 = round((hero.y + 12) / 20)
        return 0 < BG_MATRIX[y1][x1] < 7 or 0 < BG_MATRIX[y2][x2] < 7