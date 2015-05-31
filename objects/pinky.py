from pygame.constants import K_DOWN, K_UP
from objects.ghost import Ghost
from objects.Container import get_object
from pacfunctions.pacfunction import get_next_directions, next_point_in_direction
import media
from objects.hero import Hero, RECT_MATRIX


class Pinky(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, media.sprites.PinkyAnim)
        self.corner_points = [(27, 16), (27, 27), (24, 27), (24, 16)]
        self.house_time = 500

    def chase_move(self): #sprawa z argumentami do przemyslenia
        if self.in_place_to_change_direction():
            self.map_point = RECT_MATRIX.get_map_point(self.area_rect)
            self.is_dot = self.is_dot_at_field()
            predicted_direction = get_next_directions(self.map_point, get_object(0).predicted_pac_man_point(4))
            shortes_direction = get_next_directions(self.map_point, get_object(0).map_point)

            if len(shortes_direction) < 4:
                self.direction = shortes_direction[0]
            else:
                self.direction = predicted_direction[0]


