from random import randint

from objects.ghost import Ghost, stupidity_decorator
from pacfunctions.pacfunction import get_next_directions
import media
from objects.hero import Hero
from media.constans import MAP_X_DIMENTION, MAP_Y_DIMENTION
from pygame.rect import Rect
from pacfunctions.paclogic import all_neighbours


class Inky(Ghost):
    def __init__(self, x, y, rect_martix, container, evenent_handler):
        super().__init__(x, y, media.sprites.InkyAnim, rect_martix, container, evenent_handler)
        self.house_time = 800
        self.color = (42, 255, 252, 128)
        self.corner_points = [(27, 27), (27, 16), (24, 16), (24, 22)]

    @stupidity_decorator
    def chase_move(self):  # sprawa z argumentami do przemyslenia
        self.new_directions = get_next_directions(self.map_point, self.get_proper_target())

    def get_proper_target(self):
        pacman = self.container.pac_man
        blinky = self.container.ghosts[0]
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
