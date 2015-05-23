from objects.container import get_object
from objects.ghost import Ghost
from pacfunctions.pacfunction import get_next_directions
import media
from objects.hero import Hero, RECT_MATRIX


class Inky(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, media.sprites.InkyAnim)

    def move_hero(self, arguments): #sprawa z argumentami do przemyslenia

        if self.in_place_to_change_direction():
            self.map_point = RECT_MATRIX.get_map_point(self.area_rect)
            self.is_dot = self.is_dot_at_field()

        super().move()

