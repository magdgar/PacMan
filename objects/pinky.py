from pygame.constants import K_DOWN, K_UP
from objects.ghost import Ghost
from objects.Container import get_object, get_pacmans, get_pacman
from pacfunctions.pacfunction import get_next_directions, next_point_in_direction
import media
from objects.hero import Hero, RECT_MATRIX


class Pinky(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, media.sprites.PinkyAnim)
        self.corner_points = [(27, 16), (27, 27), (24, 27), (24, 16)]
        self.house_time = 400

    def chase_move(self): #sprawa z argumentami do przemyslenia
        if self.in_place_to_change_direction():
            self.map_point = RECT_MATRIX.get_map_point(self.area_rect)
            self.is_dot = self.is_dot_at_field()
            predicted_directions = self.get_directions_to_closest_predicted_pacman()
            shortes_directions = self.get_directions_to_closest_pacman()

            if len(shortes_directions) < 4:
                self.direction = shortes_directions[0]
            else:
                self.direction = predicted_directions[0]


    def get_directions_to_closest_predicted_pacman(self):
        if len(get_pacmans()) == 1:
            self.new_directions = get_next_directions(self.map_point, get_pacman(0).predicted_pac_man_point(4))
        else:
            directions_to_player = get_next_directions(self.map_point, get_pacman(0).predicted_pac_man_point(4))
            directions_to_enemy = get_next_directions(self.map_point, get_pacman(1).predicted_pac_man_point(4))
            self.new_directions = directions_to_player if len(directions_to_player) <= len(directions_to_enemy) else directions_to_enemy
        return self.new_directions
