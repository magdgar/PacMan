from pygame.constants import K_DOWN, K_UP
from objects.ghost import Ghost, stupidity_decorator

from pacfunctions.pacfunction import get_next_directions, next_point_in_direction
import media
from objects.hero import Hero


class Pinky(Ghost):
    def __init__(self, x, y, rect_martix, container, evenent_handler):
        super().__init__(x, y, media.sprites.PinkyAnim, rect_martix, container, evenent_handler)
        self.corner_points = [(1, 2),  (5, 2), (5, 7), (2, 7)]
        self.color = (255, 156, 200, 128)
        self.house_time = 400

    @stupidity_decorator
    def chase_move(self): #sprawa z argumentami do przemyslenia
        self.new_directions = self.get_directions_to_closest_predicted_pacman()

    def get_directions_to_closest_predicted_pacman(self):
        if self.container.enemy_pac_man is None:
            return get_next_directions(self.map_point, self.container.pac_man.predicted_pac_man_point(4))
        else:
            if self.container.pac_man.active:
                directions_to_player = get_next_directions(self.map_point, self.container.pac_man.predicted_pac_man_point(4))
            else:
                directions_to_player = [self.get_proper_random_direction()]
            if self.container.enemy_pac_man.active:
                directions_to_enemy = get_next_directions(self.map_point, self.container.enemy_pac_man.predicted_pac_man_point(4))
            else:
                directions_to_enemy = [self.get_proper_random_direction()]

            if len(directions_to_enemy) == 0 and len(directions_to_player) == 0:
                return [self.get_proper_random_direction()]

            self.new_directions = directions_to_player if len(directions_to_player) <= len(directions_to_enemy) else directions_to_enemy
        return self.new_directions
