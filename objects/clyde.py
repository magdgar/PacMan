
from pacfunctions.pacfunction import get_next_directions
import media
from objects.ghost import Ghost, stupidity_decorator


class Clyde(Ghost):
    def __init__(self, x, y, rect_martix, container, evenent_handler):
        super().__init__(x, y, media.sprites.ClydeAnim, rect_martix, container, evenent_handler)
        self.house_time = 1200
        self.color = (255, 198, 56, 128)
        self.corner_points = [(27, 2), (27, 13), (24, 13), (24, 7)]

    @stupidity_decorator
    def chase_move(self): #sprawa z argumentami do przemyslenia
        self.new_directions = self.get_directions()

    def get_directions(self):
        directions_to_pacman = self.get_directions_to_closest_pacman()
        directions_to_left_corner = get_next_directions(self.map_point, (27, 2))
        if len(directions_to_pacman) <= 8:
            self.stupidity = len(directions_to_left_corner)
            return directions_to_left_corner
        else:
            self.stupidity = 6
            return directions_to_pacman
