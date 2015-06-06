from objects.ghost import Ghost
from objects.Container import get_object, get_pacmans, get_pacman
from objects.hero import RECT_MATRIX
from pacfunctions.pacfunction import get_next_directions
import media


class Blinky(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, media.sprites.BlinkyAnim)
        self.corner_points = [(1, 26), (5, 26), (5, 15), (1, 15)]
        self.house_time = 10

    def chase_move(self): #sprawa z argumentami do przemyslenia

        if self.in_place_to_change_direction():
            self.map_point = RECT_MATRIX.get_map_point(self.area_rect)
            self.is_dot = self.is_dot_at_field()
            if self.change_direction_counter % self.stupidity == 0:
                self.change_direction_counter = 1
                self.new_directions = self.get_directions_to_closest_pacman()
                # self.has_catched_pacman(self.new_directions)
                self.direction = self.new_directions[0]
            else:
                if self.change_direction_counter < len(self.new_directions):
                    self.direction = self.new_directions[self.change_direction_counter]
                else:
                    self.direction = self.get_proper_random_direction()
                self.change_direction_counter += 1

