from objects.ghost import Ghost
from objects.Container import get_object
from objects.hero import RECT_MATRIX
from pacfunctions.pacfunction import get_next_directions
import media


class Blinky(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, media.sprites.BlinkyAnim)
        self.corner_points = [(1, 1), (1, 12), (5, 12), (5, 1)]
        self.house_time = 250

    def chase_move(self): #sprawa z argumentami do przemyslenia

        if self.in_place_to_change_direction():
            self.map_point = RECT_MATRIX.get_map_point(self.area_rect)
            self.is_dot = self.is_dot_at_field()
            if self.change_direction_counter % self.stupidity == 0:
                self.change_direction_counter = 1
                self.new_directions = get_next_directions(self.map_point, get_object(0).map_point)
                # self.has_catched_pacman(self.new_directions)
                self.direction = self.new_directions[0]
            else:
                if self.change_direction_counter < len(self.new_directions):
                    self.direction = self.new_directions[self.change_direction_counter]
                else:
                    self.direction = self.get_proper_random_direction()
                self.change_direction_counter += 1

