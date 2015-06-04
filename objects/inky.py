from functools import wraps
from random import randint
from objects.Container import get_object
from objects.ghost import Ghost
from pacfunctions.pacfunction import get_next_directions
import media
from objects.hero import Hero, RECT_MATRIX
from media.constans import MAP_X_DIMENTION, MAP_Y_DIMENTION
from pygame.rect import Rect
from pacfunctions.paclogic import all_neighbours


class Inky(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, media.sprites.InkyAnim)
        self.house_time = 700
        self.corner_points = [(27, 27), (27, 16), (24, 16), (24, 22)]

    def chase_move(self):  # sprawa z argumentami do przemyslenia

        if self.in_place_to_change_direction():
            self.map_point = RECT_MATRIX.get_map_point(self.area_rect)
            self.is_dot = self.is_dot_at_field()
            if self.change_direction_counter % self.stupidity == 0:
                self.change_direction_counter = 1
                self.new_directions = get_next_directions(self.map_point, self.get_proper_target())
                # self.has_catched_pacman(self.new_directions)
                self.direction = self.new_directions[0]
            else:
                if self.change_direction_counter < len(self.new_directions):
                    self.direction = self.new_directions[self.change_direction_counter]
                else:
                    self.direction = self.get_proper_random_direction()
                self.change_direction_counter += 1

    @staticmethod
    def get_proper_target():
        pacman = get_object(0)
        blinky = get_object(1)
        x = blinky.map_point[1] - pacman.map_point[1]
        y = blinky.map_point[0] - pacman.map_point[0]
        target_x = pacman.map_point[1] - 2 * x
        target_y = pacman.map_point[1] - 2 * y

        if target_x <= 0:
            target_x = 2
        if target_x >= MAP_X_DIMENTION:
            target_x = MAP_X_DIMENTION - 2

        if target_y <= 0:
            target_y = 2

        if target_y >= MAP_Y_DIMENTION:
            target_y = MAP_Y_DIMENTION - 2

        res = (target_y, target_x)
        neighbours = all_neighbours(res)
        len = neighbours.__len__()
        if len == 0:
            return pacman.map_point
        else:
            return neighbours.pop(randint(0, len-1))
